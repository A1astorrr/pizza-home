/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/templates/**/*.{html,js}"],
  theme: {
    extend: {fontFamily: {
      'AC': "Kaph Italic"
    }, padding: {'0.5-1rem': "0.5rem 1rem"},
   colors: {"bb": "#c53a0336"}, gridTemplateColumns: {"auto": "auto auto auto"}, transitionProperty: {"transform": "transform 0.5s ease"}, margin: {"0-auto-1": "0 auto 1rem"}, transitionProperty: {"bg": "background 0.3s"},},
  },
  plugins: [],
}