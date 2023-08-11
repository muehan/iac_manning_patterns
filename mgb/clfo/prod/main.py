import sys
sys.path.insert(1, '../../../modules/azure')

from resourcegroup import ResourceFactoryModule
from network import NetworkFactoryModule
from subnet import SubnetFactoryModule
from networkinterface import NetworkInterfaceFactoryModule
from vm import VmFactoryModule

import json

if __name__ == "__main__":

    location = "Sitzerland North"
    with open('C:\\temp\\key\\.ssh\\id_rsa.pub') as f:
        key = f.readline()

    resourceGroup = ResourceFactoryModule(location, "DevelopmentResource")
    network = NetworkFactoryModule(
        location, "dev-network", resourceGroup, "10.0.0.0/16")
    subnet = SubnetFactoryModule("dev-subnet", resourceGroup, "10.0.2.0/24")
    interface = NetworkInterfaceFactoryModule(
        location, "dev-interface", resourceGroup)

    vm1 = VmFactoryModule(location, "MyFancyVm1", key, resourceGroup)
    vm2 = VmFactoryModule(location, "MyFancyVm2", key, resourceGroup)
    vm3 = VmFactoryModule(location, "MyFancyVm3", key, resourceGroup)

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
        "resource": resourceGroup.build() + network.build() + subnet.build() + interface.build() + vm1.build() + vm2.build() + vm3.build()
    }

    with open('main.tf.json', 'w') as outfile:
        json.dump(resource, outfile, sort_keys=True, indent=4)
