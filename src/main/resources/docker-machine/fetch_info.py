#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from overtherepy import LocalConnectionOptions, OverthereHost, OverthereHostSession
from com.xebialabs.overthere import OperatingSystemFamily
import re
import sys
import traceback



def to_map(stdout):
    _data = {}
    for s in stdout:
        if 'export' in s:
            info = s.replace('export ', ' ').replace('"', ' ').strip().split('=')
            _data[str(info[0])] = str(info[1]).strip()
    return _data


def machine_name(ci):
    if ci.machineName is not None:
        return ci.machineName
    else:
        return ci.name


def docker_machine_env(machine_name):
    print "Env docker '{0}' machine ".format(machine_name)
    command_line = "docker-machine env {0}".format(machine_name)

    local_opts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
    host = OverthereHost(local_opts)
    session = OverthereHostSession(host)

    print "Executing '{0}'....".format(command_line)
    try:

        response = session.execute(command_line)
        return to_map(response.stdout)
    except:
        tb = traceback.format_exc()
        print "Error"
        print tb
    finally:
        session.close_conn()


machine_name = machine_name(target)
print "Machine name is {0}".format(machine_name)
data = docker_machine_env(machine_name=machine_name)
ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', data['DOCKER_HOST'])
if len(ip) == 1:
    data['address'] = ip[0]
print "IP Address is %s " % data['address']
print "--------------------"
print data
print "--------------------"

deployed.docker_host_address = data['address']
deployed.docker_host = data['DOCKER_HOST']
deployed.docker_cert_path = data['DOCKER_CERT_PATH']
if data['DOCKER_TLS_VERIFY'] == '1':
    deployed.docker_tls_verify = True
else:
    deployed.docker_tls_verify = False

if deployed.machineName is None:
    deployed.machineName = deployed.name


