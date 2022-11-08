class NetworkFactoryModule():
    def __init__(self, location, name, subnetName, resourceGroup):
        self._name = name
        self._location = location
        self._subnetName = subnetName
        self._resourceGroup = resourceGroup
       
    def build(self):
        return [
                {
                    "azurerm_virtual_network": [
                        {
                        "example": [
                            {
                            "address_space": [
                                "10.0.0.0/16"
                            ],
                            "location": self._location,
                            "name": self._name,
                            "resource_group_name": self._resourceGroup._name
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "azurerm_subnet": [
                        {
                        "example": [
                            {
                            "address_prefixes": [
                                "10.0.2.0/24"
                            ],
                            "name": self._subnetName,
                            "resource_group_name": self._resourceGroup._name,
                            "virtual_network_name": "${azurerm_virtual_network.example.name}"
                            }
                        ]
                        }
                ]
            },
        ]

    def outputs(self):
        return self._name, self._subnetName