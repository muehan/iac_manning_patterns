class VmFactoryModule():
    def __init__(self, location, name, key, resourceGroup):
        self._name = name
        self._location = location
        self._resourceGroup = resourceGroup
        self._key = key
       
    def build(self):
        return [
            {
                "azurerm_linux_virtual_machine": [
                    {
                    "example": [
                        {
                        "admin_username": "adminuser",
                        "network_interface_ids": [
                            "${azurerm_network_interface.example.id}"
                        ],
                        "location": self._location,
                        "name": self._name,
                        "admin_ssh_key": [
                            {
                            "username": "adminuser",
                            "public_key": self._key
                            }
                        ],
                        "os_disk": [
                            {
                            "caching": "ReadWrite",
                            "storage_account_type": "Standard_LRS"
                            }
                        ],
                        "resource_group_name": self._resourceGroup._name,
                        "size": "Standard_F2",
                        "source_image_reference": [
                            {
                            "offer": "UbuntuServer",
                            "publisher": "Canonical",
                            "sku": "16.04-LTS",
                            "version": "latest"
                            }
                        ]
                        }
                    ]
                    }
                ]
            }
        ]

    def outputs(self):
        return self._name