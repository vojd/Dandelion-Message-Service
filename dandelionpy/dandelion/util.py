"""
Copyright (c) 2011 Anders Sundman <anders@4zm.org>

This file is part of dandelionpy

dandelionpy is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

dandelionpy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with dandelionpy.  If not, see <http://www.gnu.org/licenses/>.
"""

import base64
import binascii

def encode_bytes(bstr):
    if not isinstance(bstr, bytes) and not isinstance(bstr, bytearray):
        raise TypeError    
    
    return base64.b64encode(bstr)
    
def decode_bytes(bstr):
    if not isinstance(bstr, bytes) and not isinstance(bstr, bytearray):
        raise TypeError    

    return base64.b64decode(bstr)

def encode_int(x):
    
    if not isinstance(x, int):
        raise TypeError
    
    if x < 0:
        raise ValueError
    
    hstr = '{0:X}'.format(x)
    
    if len(hstr) % 2 != 0:
        hstr = ''.join(['0', hstr])

    return base64.b64encode(binascii.a2b_hex(hstr))

def decode_int(bstr):
    if not isinstance(bstr, bytes) and not isinstance(bstr, bytearray):
        raise TypeError    

    return int(binascii.b2a_hex(base64.b64decode(bstr)), 16)
