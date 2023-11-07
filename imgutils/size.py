# Copyright (C) 2023 H. Turgut Uyar <uyar@tekir.org>
#
# imgutils is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# imgutils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with imgutils.  If not, see <http://www.gnu.org/licenses/>.

from PIL import Image


def get_width(img_file):
    with Image.open(img_file) as img:
        width = img.width
    return width


def get_height(img_file):
    with Image.open(img_file) as img:
        height = img.height
    return height


def get_aspect_ratio(img_file):
    with Image.open(img_file) as img:
        width = img.width
        height = img.height
    return width / height
