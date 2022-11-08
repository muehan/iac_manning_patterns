class NetworkInterfaceFactoryModule():
    def __init__(self, location, name, resourceGroup):
        self._name = name
        self._location = location
        self._resourceGroup = resourceGroup
       
    def build(self):
        return [
             {
                "azurerm_network_interface": [
                    {
                    "example": [
                        {
                        "ip_configuration": [
                            {
                            "name": "internal",
                            "subnet_id": "${azurerm_subnet.example.id}",
                            "private_ip_address_allocation": "Dynamic"
                            }
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
        return self._name