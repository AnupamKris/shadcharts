// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  ssr: false,
  modules: [
    "@nuxtjs/tailwindcss",
    "shadcn-nuxt",
    "nuxt-lucide-icons",
    "@nuxtjs/color-mode",
  ],
  plugins: ["~/plugins/vue-apexcharts.client.js"],
  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: "",
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: "./components/ui",
  },
  lucide: {
    namePrefix: "I",
  },
  colorMode: {
    classSuffix: "",
  },
});
