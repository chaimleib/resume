#!/usr/bin/env python

'''
postprocess.py

Given an HTML file, hides private data from bots, and turns contact data into
links for humans with browsers.
'''

import html
import json
import sys
from os import path
from xml.dom import minidom
from collections import namedtuple, deque

def embed_css(doc, dirname):
    headList = doc.getElementsByTagName('head')
    if not headList:
        head = doc.createElement('head')
        root = doc.documentElement
        root.insertBefore(head, root.firstChild)
        headList = [head]
    head = headList[0]
    for link in head.getElementsByTagName('link'):
        if link.getAttribute('rel') != 'stylesheet':
            continue
        href = link.getAttribute('href')
        if not href:
            continue
        with open(href, 'r') as file:
            css = file.read()
            doc = minidom.parseString("\n".join([
                "<style>",
                "{}",
                "</style>"
            ]).format(css))
            style = doc.documentElement
            head.replaceChild(style, link)

def nest_div(doc):
    bodyList = doc.getElementsByTagName('body')
    if not bodyList:
        body = doc.createElement('body')
        doc.documentElement.appendChild(body)
        bodyList = [body]
    body = bodyList[0]
    children = [*body.childNodes]
    div = doc.createElement('div')
    div.setAttribute('class', 'content')
    body.appendChild(div)
    for child in children:
        body.removeChild(child)
        div.appendChild(child)

_stack_node = namedtuple("StackNode", "node, addr")
def StackNode(node):
    return _stack_node(node, node.tagName)

def getElementsByClassName(doc, classname):
    stack=deque([ StackNode(doc.documentElement) ])
    result=deque()
    while bool(stack):
        node, addr = stack.pop()
        if classname in node.getAttribute("class").split():
            result.append(node)
        stack.extend(
                StackNode(child) for child in node.childNodes
                if child.nodeType not in [
                    node.TEXT_NODE,
                    node.COMMENT_NODE,
                    node.CDATA_SECTION_NODE,
                ])
    return result

def link_mailto(doc):
    for el in getElementsByClassName(doc, "link-mailto"):
        for child in [*el.childNodes]:
            if child.nodeType != el.TEXT_NODE:
                continue
            email = child.data
            link = '<a href="{0}{1}">{2}</a>'.format(
                entity_obfuscate("mailto:"),
                entity_obfuscate(url_obfuscate(email)),
                html_obfuscate(email))
            js = jswrite(link)
            el.replaceChild(js, child)

def link_tel(doc):
    for el in getElementsByClassName(doc, "link-tel"):
        for child in [*el.childNodes]:
            if child.nodeType != el.TEXT_NODE:
                continue
            normalized = html.unescape(child.data
                                       .replace('&ndash;', '')
                                       .replace('\u2013', '')
                                       .replace('-', ''))
            link = '<a href="{0}{1}">{2}</a>'.format(
                entity_obfuscate("tel:"),
                entity_obfuscate(url_obfuscate('+1{}'.format(normalized))),
                html_breakup(child.data)) # child.data already obfuscated
            js = jswrite(link)
            el.replaceChild(js, child)

def jswrite(s):
    chars = deque()
    ll = [0]
    def push(item):
        quoted = json.dumps(
            item.replace("'", '&quot;'))
        ll[0] += len(quoted)
        if ll[0] > 80:
            indent = "    "
            chars.append("\n" + indent)
            ll[0] = len(indent) + len(quoted)
        chars.append(quoted)

    for char in s:
        if len(chars) > 0:
            chars.append('+')
            ll[0] += 1
        push(char)
    outStr = ''.join([char for char in chars])
    doc = minidom.parseString("\n".join([
        "<script>",
        "//<![CDATA[",
        "  document.write({});",
        "//]]>",
        "</script>"
    ]).format(outStr))
    return doc.documentElement

def numeric_entity(c):
    return '&#{};'.format(ord(c))

def entity_obfuscate(s):
    result = deque()
    for i, c in enumerate(s):
        if c == '@':
            result.append('&commat;')
        elif not c.isalnum():
            result.append(numeric_entity(c))
        elif i & 0x1:
            result.append(numeric_entity(c))
        else:
            result.append(c)
    return ''.join(char for char in result)

def html_breakup(s):
    result = deque()
    word = ''
    i = 0
    for c in s:
        boundary = False
        if c == '&':
            word = c
        elif not word:
            result.append(c)
            i += 1
            boundary = True
        elif c == ';':
            word += c
            result.append(html.unescape(word))
            i += 1
            boundary = True
            word = ''
        else:
            word += c
        if boundary and 0x1 & i:
            result.append('<!-- {:04X} -->'.format(i))
    return ''.join(char for char in result)

def html_obfuscate(s):
    result = deque()
    for i, c in enumerate(s):
        if i & 0x1:
            result.append(entity_obfuscate(c))
        else:
            result.append(c)
        if i & 0x5:
            result.append('<!-- {:04X} -->'.format(i))
    return ''.join(char for char in result)

def html_unobfuscate(s):
    result = deque()
    word = ''
    for c in s:
        if c == '&':
            word = c
        elif not word:
            result.append(c)
        elif c == ';':
            word += c
            result.append(html.unescape(word))
            word = ''
        else:
            word += c
    return ''.join(char for char in result)

def url_obfuscate(s):
    result = deque()
    for i, c in enumerate(s):
        if i & 0x1 or c in '@.':
            result.append('%{:2X}'.format(ord(c)))
        else:
            result.append(c)
    return ''.join(char for char in result)

if __name__ == "__main__":
    def usage():
        print("\n".join([
            'usage: {} inputFile [ -o outputFile ]',
            '',
            'Obfuscates HTML to hide private information from bots while turning them into links in the browser.',
            '',
            'If outputFile is -, output is printed to stdout. This is the default.',
            '',
            'Special HTML classes:',
            '  link-mailto',
            '    Turns the unobfuscated child text into a mailto: link and obfuscates the link href and the displayed text.',
            '',
            '  link-tel',
            '    Turns the obfuscated child text into a tel: link and obfuscates the link href. The child text gets broken up with invisible elements.',
            '']))

    inputFile = ''
    outputFile = '-'
    expecting = 'default'
    for arg in sys.argv[1:]:
        if expecting == 'default':
            if arg == '-o':
                expecting = 'outputFile'
            elif arg == '-h':
                usage()
                exit(0)
            else:
                inputFile = arg
        elif expecting == 'outputFile':
            outputFile = arg
        else:
            print('error: unexpected value for expected\n')
            usage()
            exit(1)

    if not inputFile or not outputFile:
        usage()
        exit(1)

    doc = minidom.parse(inputFile)
    nest_div(doc)
    embed_css(doc, path.dirname(inputFile))
    link_mailto(doc)
    link_tel(doc)
    newDoc = doc.documentElement.toxml()
    if outputFile == '-':
        print(newDoc + '\n')
    else:
        with open(outputFile, 'w') as file:
            file.write(newDoc)

