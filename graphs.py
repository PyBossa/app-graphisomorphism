# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import json
import glob


def get(folder='graphs'):
    """
    Get graphs from folder
    :arg string folder: Folder with graphs in JSON format.
    :returns: A list of graphs.
    :rtype: list
    """
    files = glob.glob(folder + '/*.json')
    graphs = []
    files.sort()
    for f in files:
        print "Processing graph: %s" % f
        with open(f, 'r') as t:
            read_data = t.read()
        graph = dict(level=json.loads(read_data),
                     filename=f)
        graphs.append(graph)
    return graphs

