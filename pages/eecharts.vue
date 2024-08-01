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
  <div class="flex flex-wrap gap-4 h-screen w-screen">
    <Card class="h-[400px] w-[400px] flex flex-col">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <EPieChart :data="pieData" :config="chartConfig" />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
    <Card class="h-[400px] w-[400px] flex flex-col">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <EPieChart :data="pieData2" :config="chartConfig" />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
    <Card class="h-[400px] w-[400px] flex flex-col">
      <CardHeader>
        <CardTitle>Traffic Sources</CardTitle>
        <CardDescription>Traffic Sources</CardDescription>
      </CardHeader>
      <CardContent class="flex-1">
        <ELineChart
          :data="data"
          :showYAxis="false"
          :zeroBoundaryGap="true"
          :area="true"
        />
      </CardContent>
      <CardFooter>Card Footer</CardFooter>
    </Card>
    <Card class="h-[400px] w-[400px] flex flex-col">
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
  { name: "Mandalay", value: 32.881921 },
  { name: "Naypyitaw", value: 34.235322 },
  { name: "Yangon", value: 32.882757 },
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

const showYAxis = ref(true);

const chartConfig = ref({
  innerRadius: 50,
  outerRadius: 90,
});
</script>

<style lang="scss" scoped></style>
