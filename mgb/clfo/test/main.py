import json
from modules.network import NetworkFactoryModule
from modules.networkinterface import NetworkInterfaceFactoryModule
import sys
sys.path.insert(1, '../../../modules/azure')

from resourcegroup import ResourceFactoryModule
from subnet import SubnetFactoryModule
from vm import VmFactoryModule

if __name__ == "__main__":
    # vm = LinuxServerAzure()
    location = "West Europe"
    with open('C:\\temp\\key\\.ssh\\id_rsa.pub') as f:
        key = f.readline()

    resourceGroup = ResourceFactoryModule(location, "DevelopmentResource")
    network = NetworkFactoryModule(location, "dev-network", resourceGroup, "10.0.0.0/16")
    subnet = SubnetFactoryModule("dev-subnet", resourceGroup, "10.0.2.0/24")
    interface = NetworkInterfaceFactoryModule(location, "dev-interface", resourceGroup)
    vm = VmFactoryModule(location, "MyFancyVm", key, resourceGroup)

    resource = {
      "provider": [
              {
              "azurerm": [
                  {
                  "features": [
                      {}
                  ]
                  }
              ]
              }
          ],
          "resource": resourceGroup.build() + network.build() + subnet.build() + interface.build() + vm.build()
    }

    with open('main.tf.json', 'w') as outfile:
        json.dump(resource, outfile, sort_keys=True, indent=4)
