class NetworkFactoryModule():
    def __init__(self, location, name, resourceGroup, addressSpace):
        self._name = name
        self._location = location
        self._resourceGroup = resourceGroup
        self._addressSpace = addressSpace
       
    def build(self):
        return [
                {
                    "azurerm_virtual_network": [
                        {
                        "example": [
                            {
                            "address_space": [
                                self._addressSpace
                            ],
                            "location": self._location,
                            "name": self._name,
                            "resource_group_name": self._resourceGroup._name
                            }
                        ]
                        }
                    ]
                },
            ]

    def outputs(self):
        return self._name, self._subnetName, self._addressPrefixes