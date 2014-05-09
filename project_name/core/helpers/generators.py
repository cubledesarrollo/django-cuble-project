# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2014 Cuble Desarrollo S.L.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
from __future__ import unicode_literals

import random
import string

from PIL import Image


def random_upper(a_string):
    """
    :param a_string
    """
    def aleatory_upper(char):
        flag = random.choice([True, False])
        if flag:
            return char.upper()
        return char

    return ''.join([aleatory_upper(character) for character in a_string])


def random_hexadecimal(length=16):
    """ Generates a random hexadecimal string.

    :param length: Lengtht of the generated string.
    """
    hexdigits = string.hexdigits
    return ''.join(random.choice(hexdigits) for _ in range(length))


def unique_random_hexadecimal(django_cls, length=16):
    """ Generates a random hexadecimal string, unique in code field from a django class model

    :param length: Length of the generated string.
    :param django_cls: Django class, it has a code field.
    """
    code = random_hexadecimal(length)
    while django_cls.objects.filter(close2me_id=code).exists():
        length += random.choice([-1, 1])
        code = random_hexadecimal(length)
    return random_upper(code)


def random_string(length=16):
    """ Generates a random alphanumeric string.

    :param length: Lengtht of the generated string.
    """
    chars = string.digits + string.ascii_letters
    return u''.join(random.choice(chars) for _ in range(length))


def random_pin(length=4):
    """ Generates a randon numeric string

    :param length: Lengtht of the generated string.
    """
    chars = string.digits
    return u''.join(random.choice(chars) for _ in range(length))


def random_image(size=(200, 200)):
    """ Generates a random PIL image, for testings propouse.

    :param size: Size of the random image generated.
    """
    color = (random.randint(0, 255), random.randint(0, 255),
             random.randint(0, 255), 0)
    return Image.new("RGBA", size, color)
