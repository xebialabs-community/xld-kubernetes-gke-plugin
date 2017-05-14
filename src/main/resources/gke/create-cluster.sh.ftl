<#--

    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.

-->
echo "Creating GKE cluster '${deployed.name}' "
<#assign cmdLine = ["gcloud","container","clusters","create",${(deployed.clusterName)!(deployed.name)}]

<#assign cmdLine = cmdLine + ["--num-nodes",${deployed.numNode}/>
<#assign cmdLine = cmdLine + ["--zone",${deployed.zone}/>

<#if (deployed.additionalZones??)>
<#assign cmdLine = cmdLine + ["--additional-zones", ${deployed.additionalZones?join(", ")}]
</if>

echo Executing <#list cmdLine as item>${item} </#list>
<#list cmdLine as item>${item} </#list>
