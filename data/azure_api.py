"""
Placeholder module for future Azure Retail Prices API integration.
"""


def get_price_from_azure_api(region: str, vm_size: str, os: str, currency: str = "INR") -> float | None:
    """
    To be implemented later with Azure Retail Prices API.
    
    This function will replace the internal price catalog when API integration is added.
    
    Args:
        region: Azure region (e.g., "southindia", "eastus")
        vm_size: VM size (e.g., "Standard_D2s_v5")
        os: Operating system ("Linux" or "Windows")
        currency: Currency code (default: "INR")
    
    Returns:
        Hourly price as float, or None if not found/error
    """
    # TODO: Implement Azure Retail Prices API integration
    # Example API endpoint: https://prices.azure.com/api/retail/prices
    # Will require API authentication and proper querying
    return None

