# Merriam-Webster Dictionary API

The Merriam-Webster Dictionary API is a simple RESTful API that allows you to scrape the Merriam-Webster website to retrieve the meanings of words. This API provides a single endpoint that accepts a query parameter for searching the meaning of words.

## Getting Started

You'll need to install Python on your machine to use this API. You'll also need to install the required packages listed in the `requirements.txt` file provided.

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/merriam-webster-api.git
   ```

2. Navigate to the project directory:

   ```shell
   cd wordwebster-api
   ```

3. Install the required packages using pip:

   ```shell
   pip install -r requirements.txt
   ```

### Usage

Once you have the API and required packages installed, you can start using it.

1. Run the API:

   ```shell
   python app.py
   ```

2. The API will be running at `http://localhost:5000`.

3. To retrieve the meaning of a word, make a GET request to the following endpoint:

   ```
   GET http://localhost:5000/dictionary?query=<word_to_search>
   ```

   Replace `<word_to_search>` with the word you want to look up.

4. The API will respond with the meaning of the word in JSON format.

### Example

Let's say you want to find the meaning of the word "example." You can do so by making the following request:

```
GET http://localhost:5000/dictionary?query=example
```

The API will respond with:

```json
{
   "word": "example",
   "definitions": "a representative form or pattern",
}
```

### Error Handling

If the word you search for is not found on the Merriam-Webster website, the API will respond with a 404 status code and a JSON message indicating that the word was not found.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome contributions that improve the functionality or documentation of the API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This API was created using Python and the Django framework.
- Special thanks to Merriam-Webster for providing the word meanings data.

If you have any questions or encounter any issues while using the API, please don't hesitate to reach out to the project maintainers. Enjoy using the Merriam-Webster Dictionary API!


