# Imgur Scanner
Finds valid imgur URLS by bruteforcing the URL.

## How it works
The script spoofs the Firefox useragent and sends a get request to a randomly generated imgur URL.
The script looks for a small difference in the html. A valid Imgur url has the `<title>Imgur: The magic of the Internet</title>`.
Invalid urls have the `<title>imgur.com</title>`

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alexander-Development/Imgur-Scanner.git
   cd Imgur-Scanner-main
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**

   ```bash
   python main.py
   ```

## Contributing
Feel free to contribute to the development of this script. Fork the repository, make your changes, and submit a pull request.
