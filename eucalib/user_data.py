# Copyright 2009-2014 Eucalyptus Systems, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
# Please contact Eucalyptus Systems, Inc., 6755 Hollister Ave., Goleta
# CA 93117, USA or visit http://www.eucalyptus.com/licenses/ if you need
# additional information or have any questions.

#
# Order matters here. We want to make sure we initialize logging before anything
# else happens. We need to initialize the logger that boto will be using.
#
import httplib2

user_data_store={}
def query_user_data():
    resp, content = httplib2.Http().request("http://169.254.169.254/latest/user-data")
    if resp['status'] != '200' or len(content) <= 0:
        raise Exception('could not query the userdata')
    lines = content.split('\n')
    content = lines[len(lines)-1]
    #format of userdata = "key1=value1;key2=value2;..."
    kvlist = content.split(';')
    for word in kvlist:
        kv = word.split('=')
        if len(kv) == 2:
            user_data_store[kv[0]]=kv[1]

def get_value(key):
    if key in user_data_store:
       return user_data_store[key]
    else:
        query_user_data()
        if key not in user_data_store:
            raise Exception('could not find %s' % key)
        return user_data_store[key]

