#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import re
import traceback
from com.xebialabs.overthere import OperatingSystemFamily
from overtherepy import LocalConnectionOptions, OverthereHost, OverthereHostSession


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


def gke_describe(name):
    command_line = "gcloud container clusters describe {0} --format=json".format(name)

    local_opts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
    host = OverthereHost(local_opts)
    session = OverthereHostSession(host)

    print "Executing '{0}'....".format(command_line)
    try:

        response = session.execute(command_line)
        return  json.loads(" ".join(response.stdout))
    except:
        tb = traceback.format_exc()
        print "Error"
        print tb
    finally:
        session.close_conn()


name = target.clusterName or target.name
print "Cluster name is {0}".format(name)
data = gke_describe(name=name)
print data
deployed.gke_host_address = data['endpoint']
deployed.gke_url = "tcp://{0}".format(data['endpoint'])
if deployed.clusterName is None:
    deployed.clusterName = deployed.name


