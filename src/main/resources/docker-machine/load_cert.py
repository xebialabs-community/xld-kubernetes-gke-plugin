#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from overtherepy import LocalConnectionOptions, OverthereHost, OverthereHostSession
from com.xebialabs.overthere import OperatingSystemFamily
import json
import sys
import traceback


def read_pem_file_to_string(pem_full_path):
    print "read {0}.....".format(pem_full_path)
    pem_file = open(pem_full_path, 'r')
    content = pem_file.read()
    pem_file.close()
    return content


def docker_machine_inspect(machine_name):
    print "Inspect docker '{0}' machine ".format(machine_name)
    command_line = "docker-machine inspect {0}".format(machine_name)

    local_opts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
    host = OverthereHost(local_opts)
    session = OverthereHostSession(host)

    print "Executing '{0}'....".format(command_line)
    try:
        response = session.execute(command_line, check_success=False)
        out = ""
        for s in response.stdout:
            out = "%s %s\n" % (out, s)
        print out

        for s in response.stderr:
            print "ERR", s

        if response.rc != 0:
            sys.exit(response.rc)

        return json.loads(out)
    except:
        tb = traceback.format_exc()
        print "Error"
        print tb
    finally:
        session.close_conn()


data = docker_machine_inspect(machine_name=deployed.machineName)
# key.pem
print data['HostOptions']["AuthOptions"]["ClientKeyPath"]
deployed.docker_keyPem = read_pem_file_to_string(data['HostOptions']["AuthOptions"]["ClientKeyPath"])
print deployed.docker_keyPem

# cert.pem
print data['HostOptions']["AuthOptions"]["ServerCertPath"]
deployed.docker_certPem = read_pem_file_to_string(data['HostOptions']["AuthOptions"]["ClientCertPath"])
print deployed.docker_certPem


# ca.pem
print data['HostOptions']["AuthOptions"]["CaCertPath"]
deployed.docker_caPem = read_pem_file_to_string(data['HostOptions']["AuthOptions"]["CaCertPath"])
print deployed.docker_caPem

