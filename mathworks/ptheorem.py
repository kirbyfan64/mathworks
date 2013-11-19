from __future__ import division
'''
Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the 'Software') to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''
from .exponent import square
import math

class theorem(object):
    def __init__(self):
        self._hypotenuse = 0
        self._legs = [0, 0]
    def setLeg(self, number, new):
        num = number - 1
        self._legs[num] = new
    def getLeg(self, number):
        leg_map = {1: (0, 1), 2: (1, 0)}
        if self._leg[number - 1] == 0:
            self._leg[leg_map[number][0]] = math.sqrt(square(self._hypotenuse) - square(self._legs[leg_map[number][1]]))
        return self._legs[number-1]
    def setHypotenuse(self, new):
        self._hypotenuse = new
    def getHypotenuse(self):
        if self._hypotenuse == 0:
            self._hypotenuse = math.sqrt(square(self._legs[0]) + square(self._legs[1]))
        return self._hypotenuse
