#!/usr/bin/env python
"""Download production images for press page"""
import urllib.request
import os

IMAGES = {
    'gorgeous.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/c9ea5a83-6ba8-4b25-8a7a-baf65a9fec4d/DSC_3512.jpg',
    'one-party-consent.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/a9f0da80-c283-4200-9c58-78036a8b4c6f/%28L-R%29+Stephanie+Shum%2C+Cynthia+Marker%2C+and+Ashlyn+Lozan',
    'dogs.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/293263e6-95b4-4246-a151-30f24119bc73/Wannabe+Studio_22.jpg',
    'revolution.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/49ab1835-42bf-4f00-9a54-fa2f03314600/red+orchid+-+revolution-28w.jpg',
    'small-world.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1580965902728-83U5PR1IQJU52V23TS8A/image-asset.jpeg',
    'strange-heart-beating.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1580965384673-G0XJL3S7NIVDVMHNEG7X/image-asset.jpeg',
    'plainclothes.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1545166530778-3LL0PCO94AXE0T8WRHHP/Plainclothes-2.jpg',
    'second-skin.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1537848753960-504EBW2PJHODG3OGGV6U/image-asset.jpeg',
    'seven-fights.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1521928725014-XX3BVMGBM0UL568W6JFD/image-asset.jpeg',
    'the-crucible.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1508603968331-6MN3GSK4KRUC68B9SLQQ/22338829_10154963777298587_5559938543168567620_o.jpg',
    'harbur-gate.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1517863192107-A6TCQDKDNKCSODOBSUSM/26992530_10155078758022461_6234752795611788082_n.jpg',
    'mother-of-smoke.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1499476437847-BS0GKYFZRSD39TG1OHJB/MotherofSmoke-4-1.jpg',
    'kin-folk.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1470187922581-M0185EP6XZ2WVTNS9QJB/image-asset.jpeg',
    'circle-machine.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1423585178093-ASD5QCM5IOBWZHD9WG6I/Circle+Machine-1333.jpg',
    'kate-and-sam.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1403299945081-3LLEZ9TV3ZKHDK11YBM0/25.jpg',
    'rewilding-genius.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1403300566844-4CPATITWKZGQWC18242E/ReWilding+Prod.+Photos-31.jpg',
    'alice.jpg': 'https://images.squarespace-cdn.com/content/v1/53a46540e4b03c89b67c0d0a/1403300239109-EFB5HMPMGXWV0Y7ZJG/Alice2013-2-XL.jpg',
}

def download_images():
    base_dir = r'P:\Scripts\my-website\build\images\press'

    # Ensure directory exists
    os.makedirs(base_dir, exist_ok=True)

    print(f"Downloading {len(IMAGES)} production images...")

    for filename, url in IMAGES.items():
        filepath = os.path.join(base_dir, filename)

        try:
            print(f"  Downloading {filename}...", end=' ')

            # Add user agent to avoid blocking
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            with urllib.request.urlopen(req) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())

            print("✓")
        except Exception as e:
            print(f"✗ Error: {e}")

    print(f"\nImages downloaded to: {base_dir}")

if __name__ == '__main__':
    download_images()
