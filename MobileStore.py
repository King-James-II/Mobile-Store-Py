# Retail Mobile Device Store Program

class MobileDevice:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Function to perform linear search
def linear_search(devices, target):
    for device in devices:
        if device.name == target:
            return device
    return None

# Function to perform binary search (requires sorted list)
def binary_search(devices, target):
    low = 0
    high = len(devices) - 1
    while low <= high:
        mid = (low + high) // 2
        if devices[mid].name == target:
            return devices[mid]
        elif devices[mid].name < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Function to perform recursive search
def recursive_search(devices, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if devices[mid].price == target:
        return devices[mid]
    elif devices[mid].price < target:
        return recursive_search(devices, target, mid + 1, high)
    else:
        return recursive_search(devices, target, low, mid - 1)

# Function to sort devices by price
def sort_devices(devices):
    return sorted(devices, key=lambda x: x.price)

# Function to display devices
def display_devices(devices):
    print("Available Mobile Devices:")
    for i, device in enumerate(devices):
        print(f"{i+1}. {device.name} - ${device.price}")

# Main function
if __name__ == "__main__":
    # Define mobile devices
    devices = [
        MobileDevice("Xiaomi Galaxy", 576),
        MobileDevice("Xiaomi One", 467),
        MobileDevice("Apple iPhone", 1484),
        MobileDevice("Samsung iPhone", 346),
        MobileDevice("Google Mi", 1437),
        MobileDevice("OnePlus Pixel", 492),
        MobileDevice("Xiaomi Galaxy", 879),
        MobileDevice("Google Mi", 1498),
        MobileDevice("Apple Pixel", 277),
        MobileDevice("Samsung iPhone", 595)
    ]

    # Display available devices
    display_devices(devices)

    # Linear search
    print("\nSearching for a device using linear search...")
    target_device = linear_search(devices, "Xiaomi One")
    if target_device:
        print(f"Device found: {target_device.name} - ${target_device.price}")
    else:
        print("Device not found.")

    # Sort devices by price
    sorted_devices = sort_devices(devices)
    print("\nDevices sorted by price:")
    display_devices(sorted_devices)

    # Binary search
    print("\nSearching for a device using binary search...")
    target_device = binary_search(sorted_devices, "Xiaomi Galaxy")
    if target_device:
        print(f"Device found: {target_device.name} - ${target_device.price}")
    else:
        print("Device not found.")

    # Recursive search within price range
    print("\nSearching for a device within a price range using recursive search...")
    price_range_devices = recursive_search(sorted_devices, 500, 0, len(sorted_devices) - 1)
    if price_range_devices:
        print("Devices within the price range of $500 to $1000:")
        for device in price_range_devices:
            print(f"{device.name} - ${device.price}")
    else:
        print("Device not found in the specified price range.")
