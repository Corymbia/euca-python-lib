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

import os
from floppy import FloppyCredential
import libconfig as config
import wsclient as ws

def write_certificate(cert_file, cert_pem):
    if not os.path.exists(cert_file):
        f_cert = open(cert_file, 'w')
        f_cert.write(cert_pem)
        f_cert.close()
        os.chmod(cert_file, 0400)

def download_server_certificate(cert_arn):
    f = FloppyCredential()
    access_key_id = config.ACCESS_KEY_ID
    secret_access_key = config.SECRET_KEY
    security_token = config.SECURITY_TOKEN
    con = ws.connect_euare(aws_access_key_id=access_key_id,
                                  aws_secret_access_key=secret_access_key, security_token=security_token)
    cert = con.download_server_certificate(f.get_instance_pub_key(), f.get_instance_pk(), f.get_iam_pub_key(),
                                           f.get_iam_token(), cert_arn)
    return cert 

class ServerCertificate(object):
    def __init__(self, cert, pk):
        self.certificate = cert
        self.pk = pk

    def get_certificate(self):
        return self.certificate

    def get_private_key(self):
        return self.pk
