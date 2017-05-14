#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
import traceback
from overtherepy import OverthereHostSession


def gke_describe(name, target):
    command_line = "gcloud container clusters describe {0} --format=json".format(name)
    print command_line
    host = target.container
    session = OverthereHostSession(host)

    print "Executing '{0}'....".format(command_line)
    try:

        response = session.execute(command_line)
        return json.loads(" ".join(response.stdout))
    except:
        tb = traceback.format_exc()
        print "Error"
        print tb
    finally:
        session.close_conn()


name = target.clusterName or target.name
print "Cluster name is {0}".format(name)
data = gke_describe(name=name, target=target)
# print data
deployed.gke_host_address = data['endpoint']
print "gke_host_address {0}".format(deployed.gke_host_address)
deployed.gke_url = "tcp://{0}".format(data['endpoint'])
print "gke_url {0}".format(deployed.gke_url)
if deployed.clusterName is None:
    deployed.clusterName = deployed.name
print "clusterName {0}".format(deployed.clusterName)
