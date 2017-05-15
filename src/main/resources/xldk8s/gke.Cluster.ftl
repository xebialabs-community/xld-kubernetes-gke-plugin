<#--

    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.

-->

<#assign target = (deployed.container)!(previousDeployed.container)/>
gcloud container clusters get-credentials ${target.clusterName}   --zone ${target.zone}  --project ${target.project}

export KUBERNETES_MASTER=${(target.url)!(target.url)}
