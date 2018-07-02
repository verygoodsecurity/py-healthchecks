## Python util to run proxy healthchecks

### Installation
```
helm repo add py-healthchecks https://raw.githubusercontent.com/verygoodsecurity/py-healthchecks/master/charts/
helm repo update
helm install py-healthchecks/py-healthchecks --name py-healthchecks --namespace=py-healthchecks -f path_to_env_vars
```
### Contribution
See [.ops/](.ops/)
