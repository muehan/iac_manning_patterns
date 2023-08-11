class SubnetFactoryModule():
    def __init__(self, name, resourceGroup, addressPrefixes):
        self._name = name
        self._resourceGroup = resourceGroup
        self._addressPrefixes = addressPrefixes

    def build(self):
        return [
            {
                "azurerm_subnet": [
                    {
                        "example": [
                            {
                                "address_prefixes": [
                                    self._addressPrefixes
                                ],
                                "name": self._name,
                                "resource_group_name": self._resourceGroup._name,
                                "virtual_network_name": "${azurerm_virtual_network.example.name}"
                            }
                        ]
                    }
                ]
            },
        ]

    def outputs(self):
        return self._name, self._subnetName, self._addressPrefixes
