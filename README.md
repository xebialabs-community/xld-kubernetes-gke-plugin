# Overview #

The Docker Machine plugin is a XL Deploy plugin.
It adds the capability for provision `docker.Engine' using [Docker Machine](https://docs.docker.com/machine/overview/).
It defines 2 control tasks to start and to stop the docker-machine

# CI status #

[![Build Status][xld-docker-machine-plugin-travis-image]][xld-docker-machine-plugin-travis-url]

[xld-docker-machine-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-docker-machine-plugin.svg?branch=master
[xld-docker-machine-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-docker-machine-plugin


# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.

Dependencies:

* XL Deploy 6.0+
* XL Deploy Docker plugin 6.1.0+
* OvertherePy 0.3+ https://github.com/xebialabs-community/overthere-pylib/releases/tag/v0.0.3

# Sample Package #

```
<?xml version="1.0" encoding="UTF-8"?>
<udm.ProvisioningPackage version="1.0" application="Machina">
    <deployables>
        <docker.MachineSpec name="/machine">
            <tags/>
            <cardinality>1</cardinality>
            <boundTemplates>
                <ci ref="/engine"/>
            </boundTemplates>
            <provisioners/>
            <driver>vmwarefusion</driver>
            <insecureRegistries>
                <value>192.168.99.100:5000</value>
            </insecureRegistries>
            <engineOptions/>
            <engineLabels/>
        </docker.MachineSpec>
    </deployables>
    <templates>
        <template.docker.Engine name="/engine">
            <childTemplates/>
            <tags/>
            <dockerHost>{{%docker_host%}}</dockerHost>
            <enableTLS>{{%docker_tls_verify%}}</enableTLS>
            <certPem>{{%docker_certPem%}}</certPem>
            <keyPem>{{%docker_keyPem%}}</keyPem>
            <caPem>{{%docker_caPem%}}</caPem>
            <machineName>{{%machineName%}}</machineName>
        </template.docker.Engine>
    </templates>
    <boundTemplates/>
</udm.ProvisioningPackage>
```

# DockerMachineDictionary #

The `docker.machine.DockerMachineDictionary` is a new kind of dictionary that will resolve the ip of all the docker machines relative to the XL Deploy server host.
The default keu prefix is `MACHINE-` (see `docker.machine.DockerMachineDictionary` hidden property).


![Screenshot](docs/docker.machine.DockerMachineDictionary.png)
