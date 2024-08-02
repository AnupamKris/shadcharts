<template>
  <!-- <Select v-model="showYAxis">
    <SelectTrigger>
      <SelectValue placeholder="Select Color Theme" />
    </SelectTrigger>
    <SelectContent>
      <SelectGroup>
        <SelectLabel>Show Y Axis</SelectLabel>
        <SelectItem :value="true">Show</SelectItem>
        <SelectItem :value="false">Hide</SelectItem>
      </SelectGroup>
    </SelectContent>
  </Select> -->
  <div class="grid grid-cols-5 grid-rows-2 gap-3 h-screen w-screen p-3">
    <Card class="h-full w-full flex flex-col col-span-1">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <EPieChart :data="pieData2" :config="chartConfig" />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
    <Card class="h-full w-full flex flex-col col-span-2">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <EBarChart
          :data="genderData"
          :showYAxis="false"
          :zeroBoundaryGap="false"
          :area="false"
        />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
    <Card class="h-full w-full flex flex-col col-span-2">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <EBarChart
          :data="barData"
          :showYAxis="false"
          :zeroBoundaryGap="false"
          :area="false"
          :showLegend="false"
        />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
    <Card class="h-full w-full flex flex-col col-span-5">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <ELineChart
          :data="lineData"
          :showYAxis="false"
          :zeroBoundaryGap="false"
          :area="true"
        />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
  </div>
</template>

<script setup>
const data = ref([
  {
    AC: 100,
    Sofa: 200,
    name: "Jan",
  },
  {
    AC: 135,
    Sofa: 241,
    name: "Feb",
  },
  {
    AC: 721,
    Sofa: 415,
    name: "Mar",
  },
  {
    AC: 125,
    Sofa: 453,
    name: "Apr",
  },
]);

const pieData = ref([
  { name: "Mandalay", value: 106197.672 },
  { name: "Naypyitaw", value: 110568.7065 },
  { name: "Yangon", value: 106200.3705 },
]);

const pieData2 = ref([
  { name: "Electronic accessories", value: 16.824497155897618 },
  { name: "Fashion accessories", value: 16.814701565454342 },
  { name: "Food and beverages", value: 17.384094236896193 },
  { name: "Health and beauty", value: 15.231827781750995 },
  { name: "Home and lifestyle", value: 16.677231686163456 },
  { name: "Sports and travel", value: 17.06764757383739 },
]);

const barData = ref([
  {
    "Electronic accessories": 333,
    "Fashion accessories": 336,
    "Food and beverages": 325,
    "Health and beauty": 254,
    "Home and lifestyle": 342,
    "Sports and travel": 375,
    name: "2019-01",
  },
  {
    "Electronic accessories": 313,
    "Fashion accessories": 295,
    "Food and beverages": 349,
    "Health and beauty": 266,
    "Home and lifestyle": 205,
    "Sports and travel": 226,
    name: "2019-02",
  },
  {
    "Electronic accessories": 325,
    "Fashion accessories": 271,
    "Food and beverages": 278,
    "Health and beauty": 334,
    "Home and lifestyle": 364,
    "Sports and travel": 319,
    name: "2019-03",
  },
]);

const lineData = ref([
  {
    Mandalay: 1536.696,
    Naypyitaw: 837.165,
    Yangon: 2371.3199999999997,
    name: "2019-01-01",
  },
  {
    Mandalay: 1162.8015,
    Naypyitaw: 475.65000000000003,
    Yangon: 307.05150000000003,
    name: "2019-01-02",
  },
  {
    Mandalay: 1016.694,
    Naypyitaw: 124.02600000000001,
    Yangon: 937.4085,
    name: "2019-01-03",
  },
  {
    Mandalay: 510.5835,
    Naypyitaw: 629.8425,
    Yangon: 483.26250000000005,
    name: "2019-01-04",
  },
  {
    Mandalay: 486.759,
    Naypyitaw: 1025.4195,
    Yangon: 2024.505,
    name: "2019-01-05",
  },
  {
    Mandalay: 1021.6395,
    Naypyitaw: 1282.596,
    Yangon: 1309.9695000000002,
    name: "2019-01-06",
  },
  {
    Mandalay: 1341.9105,
    Naypyitaw: 386.379,
    Yangon: 1105.9544999999998,
    name: "2019-01-07",
  },
  {
    Mandalay: 2208.948,
    Naypyitaw: 2401.329,
    Yangon: 683.4555,
    name: "2019-01-08",
  },
  {
    Mandalay: 168.525,
    Naypyitaw: 2650.4835,
    Yangon: 202.335,
    name: "2019-01-09",
  },
  {
    Mandalay: 1348.599,
    Naypyitaw: 1480.857,
    Yangon: 731.4929999999999,
    name: "2019-01-10",
  },
  { Naypyitaw: 453.2955, Yangon: 1661.667, name: "2019-01-11" },
  {
    Mandalay: 2312.142,
    Naypyitaw: 1443.5819999999999,
    Yangon: 1429.0395,
    name: "2019-01-12",
  },
  {
    Mandalay: 735.105,
    Naypyitaw: 603.6975,
    Yangon: 1112.4015,
    name: "2019-01-13",
  },
  {
    Mandalay: 1191.4875,
    Naypyitaw: 1679.034,
    Yangon: 1096.095,
    name: "2019-01-14",
  },
  {
    Mandalay: 2862.363,
    Naypyitaw: 1275.2354999999998,
    Yangon: 1806.6615,
    name: "2019-01-15",
  },
  {
    Mandalay: 885.549,
    Naypyitaw: 2540.475,
    Yangon: 863.058,
    name: "2019-01-16",
  },
  {
    Mandalay: 993.1635,
    Naypyitaw: 647.367,
    Yangon: 1502.2245,
    name: "2019-01-17",
  },
  {
    Mandalay: 276.36,
    Naypyitaw: 1344.2835,
    Yangon: 1159.83,
    name: "2019-01-18",
  },
  {
    Mandalay: 633.486,
    Naypyitaw: 1026.753,
    Yangon: 3254.4855,
    name: "2019-01-19",
  },
  {
    Mandalay: 230.286,
    Naypyitaw: 1700.202,
    Yangon: 1724.9609999999998,
    name: "2019-01-20",
  },
  {
    Mandalay: 103.0365,
    Naypyitaw: 697.326,
    Yangon: 1591.737,
    name: "2019-01-21",
  },
  {
    Mandalay: 503.118,
    Naypyitaw: 399.37800000000004,
    Yangon: 802.2735,
    name: "2019-01-22",
  },
  { Naypyitaw: 3632.874, Yangon: 2361.3135, name: "2019-01-23" },
  {
    Mandalay: 2608.935,
    Naypyitaw: 333.93149999999997,
    Yangon: 2459.184,
    name: "2019-01-24",
  },
  {
    Mandalay: 1601.25,
    Naypyitaw: 2185.2915000000003,
    Yangon: 913.8255,
    name: "2019-01-25",
  },
  {
    Mandalay: 3203.277,
    Naypyitaw: 839.2334999999999,
    Yangon: 415.00199999999995,
    name: "2019-01-26",
  },
  {
    Mandalay: 918.4770000000001,
    Naypyitaw: 2043.1425,
    Yangon: 1674.2775000000001,
    name: "2019-01-27",
  },
  {
    Mandalay: 3130.3754999999996,
    Naypyitaw: 1581.4785000000002,
    Yangon: 287.8575,
    name: "2019-01-28",
  },
  {
    Mandalay: 946.5540000000001,
    Naypyitaw: 1045.0965,
    Yangon: 1524.915,
    name: "2019-01-29",
  },
  {
    Mandalay: 455.65799999999996,
    Naypyitaw: 1807.1970000000001,
    Yangon: 295.407,
    name: "2019-01-30",
  },
  {
    Mandalay: 2782.2795,
    Naypyitaw: 1862.0595,
    Yangon: 588.1575,
    name: "2019-01-31",
  },
  { Naypyitaw: 1532.601, Yangon: 911.9354999999999, name: "2019-02-01" },
  {
    Mandalay: 1609.2825,
    Naypyitaw: 1511.7060000000001,
    Yangon: 1019.9594999999999,
    name: "2019-02-02",
  },
  {
    Mandalay: 1037.4945,
    Naypyitaw: 1713.0749999999998,
    Yangon: 2717.358,
    name: "2019-02-03",
  },
  {
    Mandalay: 1054.5465,
    Naypyitaw: 145.5615,
    Yangon: 1239.3885,
    name: "2019-02-04",
  },
  {
    Mandalay: 989.6460000000001,
    Naypyitaw: 1473.0555,
    Yangon: 568.428,
    name: "2019-02-05",
  },
  {
    Mandalay: 1080.6705,
    Naypyitaw: 1401.561,
    Yangon: 423.192,
    name: "2019-02-06",
  },
  {
    Mandalay: 2723.3115,
    Naypyitaw: 2438.2889999999998,
    Yangon: 2066.61,
    name: "2019-02-07",
  },
  {
    Mandalay: 1755.453,
    Naypyitaw: 1634.85,
    Yangon: 1694.3535,
    name: "2019-02-08",
  },
  {
    Mandalay: 1045.1175,
    Naypyitaw: 1628.697,
    Yangon: 598.0799999999999,
    name: "2019-02-09",
  },
  {
    Mandalay: 688.359,
    Naypyitaw: 1429.995,
    Yangon: 1022.6685,
    name: "2019-02-10",
  },
  {
    Mandalay: 1847.9265,
    Naypyitaw: 2043.9825,
    Yangon: 650.244,
    name: "2019-02-11",
  },
  {
    Mandalay: 1472.352,
    Naypyitaw: 969.5174999999999,
    Yangon: 557.1195,
    name: "2019-02-12",
  },
  {
    Mandalay: 326.193,
    Naypyitaw: 391.9335,
    Yangon: 216.111,
    name: "2019-02-13",
  },
  {
    Mandalay: 759.696,
    Naypyitaw: 621.5790000000001,
    Yangon: 1072.8165,
    name: "2019-02-14",
  },
  {
    Mandalay: 3214.8165,
    Naypyitaw: 2392.761,
    Yangon: 1223.208,
    name: "2019-02-15",
  },
  {
    Mandalay: 1238.748,
    Naypyitaw: 1082.5919999999999,
    Yangon: 182.427,
    name: "2019-02-16",
  },
  {
    Mandalay: 851.151,
    Naypyitaw: 1377.4635,
    Yangon: 3070.956,
    name: "2019-02-17",
  },
  {
    Mandalay: 30.996,
    Naypyitaw: 533.2845,
    Yangon: 931.749,
    name: "2019-02-18",
  },
  {
    Mandalay: 470.988,
    Naypyitaw: 1693.8075,
    Yangon: 2063.3235,
    name: "2019-02-19",
  },
  {
    Mandalay: 1712.802,
    Naypyitaw: 90.5835,
    Yangon: 903.0315,
    name: "2019-02-20",
  },
  {
    Mandalay: 435.7605,
    Naypyitaw: 659.862,
    Yangon: 298.116,
    name: "2019-02-21",
  },
  {
    Mandalay: 1172.6295,
    Naypyitaw: 760.515,
    Yangon: 509.16599999999994,
    name: "2019-02-22",
  },
  {
    Mandalay: 1226.652,
    Naypyitaw: 804.363,
    Yangon: 308.574,
    name: "2019-02-23",
  },
  {
    Mandalay: 763.014,
    Naypyitaw: 1436.589,
    Yangon: 522.8580000000001,
    name: "2019-02-24",
  },
  {
    Mandalay: 2498.1495,
    Naypyitaw: 502.7505,
    Yangon: 1806.336,
    name: "2019-02-25",
  },
  {
    Mandalay: 2035.3725,
    Naypyitaw: 216.6885,
    Yangon: 156.1035,
    name: "2019-02-26",
  },
  {
    Mandalay: 1888.383,
    Naypyitaw: 1529.367,
    Yangon: 2441.7015,
    name: "2019-02-27",
  },
  { Mandalay: 494.76, Naypyitaw: 917.952, Yangon: 684.306, name: "2019-02-28" },
  {
    Mandalay: 933.3135,
    Naypyitaw: 1056.8355000000001,
    Yangon: 644.217,
    name: "2019-03-01",
  },
  {
    Mandalay: 3572.2574999999997,
    Naypyitaw: 2346.5924999999997,
    Yangon: 641.4555,
    name: "2019-03-02",
  },
  {
    Mandalay: 1813.749,
    Naypyitaw: 2224.908,
    Yangon: 814.5165000000001,
    name: "2019-03-03",
  },
  {
    Mandalay: 181.818,
    Naypyitaw: 860.832,
    Yangon: 2851.7895,
    name: "2019-03-04",
  },
  {
    Mandalay: 3540.0015000000003,
    Naypyitaw: 2272.1895,
    Yangon: 418.6875,
    name: "2019-03-05",
  },
  {
    Mandalay: 2020.4205,
    Naypyitaw: 38.85,
    Yangon: 1033.326,
    name: "2019-03-06",
  },
  {
    Mandalay: 297.906,
    Naypyitaw: 771.6659999999999,
    Yangon: 368.6865,
    name: "2019-03-07",
  },
  {
    Mandalay: 92.5575,
    Naypyitaw: 1440.558,
    Yangon: 1592.2725,
    name: "2019-03-08",
  },
  {
    Mandalay: 3006.486,
    Naypyitaw: 1687.371,
    Yangon: 2780.19,
    name: "2019-03-09",
  },
  {
    Mandalay: 341.26050000000004,
    Naypyitaw: 1342.7715,
    Yangon: 1479.1979999999999,
    name: "2019-03-10",
  },
  {
    Mandalay: 483.336,
    Naypyitaw: 766.7415,
    Yangon: 1711.1744999999999,
    name: "2019-03-11",
  },
  {
    Mandalay: 1392.3944999999999,
    Naypyitaw: 1361.703,
    Yangon: 923.454,
    name: "2019-03-12",
  },
  {
    Mandalay: 423.885,
    Naypyitaw: 851.613,
    Yangon: 788.109,
    name: "2019-03-13",
  },
  {
    Mandalay: 2013.9945,
    Naypyitaw: 3449.0295,
    Yangon: 1751.6100000000001,
    name: "2019-03-14",
  },
  {
    Mandalay: 1749.7725,
    Naypyitaw: 548.184,
    Yangon: 644.4585,
    name: "2019-03-15",
  },
  {
    Mandalay: 841.2915,
    Naypyitaw: 1270.479,
    Yangon: 1042.7024999999999,
    name: "2019-03-16",
  },
  {
    Mandalay: 450.009,
    Naypyitaw: 393.246,
    Yangon: 1133.034,
    name: "2019-03-17",
  },
  {
    Mandalay: 453.033,
    Naypyitaw: 450.1875,
    Yangon: 389.613,
    name: "2019-03-18",
  },
  {
    Mandalay: 599.6025,
    Naypyitaw: 3248.658,
    Yangon: 1892.1315,
    name: "2019-03-19",
  },
  {
    Mandalay: 1683.8115,
    Naypyitaw: 1401.9285,
    Yangon: 2372.4645,
    name: "2019-03-20",
  },
  {
    Mandalay: 207.858,
    Naypyitaw: 360.927,
    Yangon: 1308.7305000000001,
    name: "2019-03-21",
  },
  { Mandalay: 1051.092, Yangon: 2128.056, name: "2019-03-22" },
  {
    Mandalay: 384.468,
    Naypyitaw: 1962.198,
    Yangon: 1748.376,
    name: "2019-03-23",
  },
  {
    Mandalay: 1564.7835,
    Naypyitaw: 1488.06,
    Yangon: 424.62,
    name: "2019-03-24",
  },
  {
    Mandalay: 418.089,
    Naypyitaw: 1277.7555,
    Yangon: 577.122,
    name: "2019-03-25",
  },
  { Mandalay: 301.203, Naypyitaw: 473.97, Yangon: 1187.34, name: "2019-03-26" },
  {
    Mandalay: 898.8945,
    Naypyitaw: 943.299,
    Yangon: 1060.626,
    name: "2019-03-27",
  },
  {
    Mandalay: 95.6655,
    Naypyitaw: 480.8055,
    Yangon: 1652.931,
    name: "2019-03-28",
  },
  {
    Mandalay: 2059.932,
    Naypyitaw: 985.6980000000001,
    Yangon: 977.613,
    name: "2019-03-29",
  },
  {
    Mandalay: 1724.4569999999999,
    Naypyitaw: 1441.9859999999999,
    Yangon: 1320.6165,
    name: "2019-03-30",
  },
]);

const genderData = ref([
  { Female: 27102.0225, Male: 27235.509, name: "Electronic accessories" },
  { Female: 30437.4, Male: 23868.495, name: "Fashion accessories" },
  { Female: 33170.9175, Male: 22973.9265, name: "Food and beverages" },
  { Female: 18560.9865, Male: 30632.7525, name: "Health and beauty" },
  { Female: 30036.8775, Male: 23825.0355, name: "Home and lifestyle" },
  {
    Female: 28574.720999999998,
    Male: 26548.105499999998,
    name: "Sports and travel",
  },
]);

const showYAxis = ref(true);

const chartConfig = ref({
  innerRadius: 50,
  outerRadius: 90,
});
</script>

<style lang="scss" scoped></style>
