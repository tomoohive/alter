module.exports = {
  "assetsDir": "static",
  "devServer": {
    "port": 8080,
    "host": "127.0.0.1",
    "proxy": "http://localhost:5000"
  },
  "transpileDependencies": [
    "vuetify"
  ]
}