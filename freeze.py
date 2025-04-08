import sys
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

def main():
    try:
        print('Starting to freeze the application...')
        freezer.freeze()
        print('Successfully generated static files in the build directory!')
        return 0
    except Exception as e:
        print(f'Error freezing the application: {e}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
