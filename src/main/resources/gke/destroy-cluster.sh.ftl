<#--

    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.

-->
echo "Destroy GKE cluster '${previousDeployed.name}' "
<#assign cmdLine = ["gcloud","container","clusters","delete",(previousDeployed.clusterName)!(previousDeployed.name)]/>
<#assign cmdLine = cmdLine + ["--zone",previousDeployed.zone]/>

echo Executing <#list cmdLine as item>${item} </#list>
yes | <#list cmdLine as item>${item} </#list>
