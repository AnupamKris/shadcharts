<template>
  <div
    class="h-screen w-screen grid grid-cols-5 gap-3 p-3 m-0 screen-template overflow-hidden"
  >
    <!-- <div class="flex w-full min-h-[40px] border-b items-center px-3">
      <div
        class="flex items-center gap-2 h-5 py-3 text-muted-foreground w-full"
      >
        <ILineChart class="h-4 w-4" />
        <p>Chart</p>
        <Button class="p-0 h-6 w-6 ml-auto" variant="outline">
          <IClipboard class="h-3 w-3" />
        </Button>
        <Separator orientation="vertical" class="h-full" />
        <Button class="p-0 px-2 h-6" variant="outline"> View Code </Button>
      </div>
    </div> -->
    <Card class="col-span-1 row-span-2">
      <CardHeader class="row-span-1">
        <CardTitle> Data Controls </CardTitle>
        <CardDescription> Settings and controls for the chart </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col gap-2">
        <Select v-model="$colorMode.preference">
          <SelectTrigger>
            <SelectValue placeholder="Select Color Theme" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectLabel>Color Theme</SelectLabel>
              <SelectItem value="system">System</SelectItem>
              <SelectItem value="light">Light</SelectItem>
              <SelectItem value="dark">Dark</SelectItem>
              <SelectItem value="sepia">Sepia</SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
        <Button variant="" @click="switchChart"> Switch Chart </Button>
        <div class="flex gap-2 justify-between">
          <Button variant="secondary" @click="addRandomData" class="w-full">
            Add Data
          </Button>
          <Button variant="outline" @click="removeRandomData" class="w-full">
            Remove Data
          </Button>
        </div>
        <div class="flex gap-2 justify-between">
          <Button class="w-full" variant="secondary" @click="addGroup">
            Add Group
          </Button>
          <Button class="w-full" variant="outline" @click="removeGroup">
            Remove Group
          </Button>
        </div>
        <Button variant="outline" @click="autoHeight = !autoHeight">
          {{ autoHeight ? "Disable" : "Enable" }} Auto Height
        </Button>
        <!-- -{{ areaData }} -->
      </CardContent>
    </Card>

    <Card class="row-span-1 flex flex-col justify-between">
      <CardHeader class="h-[90px]">
        <CardTitle> Area Chart - Stacked </CardTitle>
        <CardDescription>
          Showing the total and prediction for each month
        </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col flex-1">
        <AreaChart
          v-if="chartVisible"
          :data="areaData?.slice(0, 5)"
          index="name"
          :categories="groups"
          class="w-full chart"
          :class="{ 'auto-height': autoHeight }"
          :showYAxis="false"
          :showGridLine="true"
          :colors="colors"
          :showLegend="true"
        />
      </CardContent>
      <CardFooter class="h-[90px]">
        <div class="flex w-full items-start gap-2 text-sm">
          <div class="grid gap-2">
            <div class="flex items-center gap-2 font-medium leading-none">
              Trending up by 5.2% this month <ITrendingUp class="h-4 w-4" />
            </div>
            <div
              class="flex items-center gap-2 leading-none text-muted-foreground"
            >
              January - June 2023
            </div>
          </div>
        </div>
      </CardFooter>
    </Card>

    <Card class="flex flex-col justify-between col-span-2">
      <CardHeader class="h-[90px]">
        <CardTitle> Line Chart - Stacked </CardTitle>
        <CardDescription>
          Showing the total and prediction for each month
        </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col flex-1">
        <LineChart
          v-if="chartVisible"
          :data="areaData"
          index="name"
          :categories="groups"
          class="w-full chart"
          :class="{ 'auto-height': autoHeight }"
          :showYAxis="false"
          :showGridLine="true"
          :colors="colors"
          :showLegend="true"
        />
      </CardContent>
      <CardFooter class="h-[90px]">
        <div class="flex w-full items-start gap-2 text-sm">
          <div class="grid gap-2">
            <div class="flex items-center gap-2 font-medium leading-none">
              Trending up by 5.2% this month <ITrendingUp class="h-4 w-4" />
            </div>
            <div
              class="flex items-center gap-2 leading-none text-muted-foreground"
            >
              January - June 2024
            </div>
          </div>
        </div>
      </CardFooter>
    </Card>
    <Card class="flex flex-col justify-between">
      <CardHeader class="h-[90px]">
        <CardTitle> Donut Chart </CardTitle>
        <CardDescription>
          Showing the total and prediction for each month
        </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col gap-2 flex-1">
        <DonutChart
          v-if="chartVisible"
          :data="areaData.slice(0, 5)"
          index="name"
          :category="groups[0]"
          class="w-full chart"
          :class="{ 'auto-height': autoHeight }"
          type="donut"
          centralLabel="Total Sales"
          :value-formatter="valueFormatter"
          :arc-width="30"
          :colors="colors"
          :showLegend="true"
        />
      </CardContent>
      <CardFooter class="h-[90px]">
        <div class="flex w-full items-start gap-2 text-sm">
          <div class="grid gap-2">
            <div class="flex items-center gap-2 font-medium leading-none">
              Trending up by 5.2% this month <ITrendingUp class="h-4 w-4" />
            </div>
            <div
              class="flex items-center gap-2 leading-none text-muted-foreground"
            >
              January - June 2024
            </div>
          </div>
        </div>
      </CardFooter>
    </Card>
    <div class="flex flex-col gap-2">
      <Card class="h-full">
        <CardContent
          class="flex flex-col gap-2 row-span-3 py-2 justify-center h-full"
        >
          <div class="flex gap-2 items-end">
            <span class="text-2xl font-bold">1,543</span>
            <p class="text-muted-foreground">steps/day</p>
          </div>

          <div class="flex gap-2 items-end">
            <span class="text-2xl font-bold">32,543</span>
            <p class="text-muted-foreground">steps/month</p>
          </div>
        </CardContent>
      </Card>
      <Card class="flex flex-col justify-between col-span-1 min-h-[250px]">
        <CardHeader class="pb-0">
          <CardTitle>Data Card</CardTitle>
          <CardDescription>Max sales for the month</CardDescription>
        </CardHeader>
        <CardContent class="flex flex-col gap-2 row-span-3 py-2 justify-center">
          <div class="flex gap-2 items-end">
            <span class="text-2xl font-bold">1,543</span>
            <p class="text-muted-foreground">steps/day</p>
          </div>

          <div class="flex gap-2 items-end">
            <span class="text-2xl font-bold">32,543</span>
            <p class="text-muted-foreground">steps/month</p>
          </div>
        </CardContent>
        <CardFooter class="p-0">
          <div class="flex w-full items-start gap-2 text-sm">
            <AreaChart
              v-if="chartVisible"
              :data="areaData?.slice(0, 3)"
              index="name"
              :categories="groups"
              class="w-full h-[80px] p-0"
              :showYAxis="false"
              :showXAxis="false"
              :showGridLine="true"
              :colors="colors"
              :containerMargin="{ top: 0, bottom: 0, left: 0, right: 0 }"
              :containerPadding="{ left: 0, right: 0, top: 0, bottom: 0 }"
              :showLegend="false"
            />
          </div>
        </CardFooter>
      </Card>
    </div>
    <Card class="flex flex-col justify-between col-span-3">
      <CardHeader class="h-[90px]">
        <CardTitle> Bar Chart - Grouped </CardTitle>
        <CardDescription>
          Showing the total and prediction for each month
        </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col gap-2 flex-1">
        <BarChart
          v-if="chartVisible"
          :data="areaData"
          index="name"
          :categories="groups"
          class="w-full chart"
          :class="{ 'auto-height': autoHeight }"
          :showYAxis="false"
          :showGridLine="true"
          :colors="colors"
          :rounded-corners="5"
        />
      </CardContent>
      <CardFooter class="h-[90px]">
        <div class="flex w-full items-start gap-2 text-sm">
          <div class="grid gap-2">
            <div class="flex items-center gap-2 font-medium leading-none">
              Trending up by 5.2% this month <ITrendingUp class="h-4 w-4" />
            </div>
            <div
              class="flex items-center gap-2 leading-none text-muted-foreground"
            >
              January - June 2024
            </div>
          </div>
        </div>
      </CardFooter>
    </Card>
  </div>
  {{ areaData }}
</template>

<script setup>
const chartVisible = ref(false);

const valueFormatter = (tick) =>
  typeof tick === "number"
    ? `$${new Intl.NumberFormat("us").format(tick).toString()}`
    : "";

const colors = [
  // "#e21d48", // Rich Burgundy (Hex code)
  // "#f17e91", // Blush Pink (Hex code)
  // "#f7abb6", // Soft Petal (Hex code)
  // "#fbd5da", // Pastel Hush Rose (Hex code)
  // "#ff9fb5", // Light Coral (Hex code)
  // "#ffd4cc", // Pale Peach (Hex code)
  // "#ffe2e3", // Creamy Hug (Hex code)
  // "#ffe6ea", // Whispered Rose (Hex code)
  // "#fff0ec", // Soft Focus (Hex code)
  // "#fff5f7", // Pastel Dream (Hex code)
  "#03a9f4", // Soft Teal (Hex code)
  "#e91e63", // Deep Magenta (Hex code)
  "#6c5ce7", // Dark Blue (Hex code)
  "#ff9800", // Vibrant Coral (Hex code)
  "#9c27b0", // Rich Plum (Hex code)
  "#8bc34a", // Light Olive (Hex code)
  "#2196f3", // Bright Sky Blue (Hex code)
  "#4caf50", // Fresh Green (Hex code)
  "#795548", // Earthy Brown (Hex code)
  "#ffc107", // Warm Orange (Hex code)
];

onMounted(() => {
  // chartVisible.value = true;
  setTimeout(() => {
    // chartVisible.value = true;
  }, 300);
  setTimeout(() => {
    // autoHeight.value = true;
  }, 600);
});

const groups = ref([]);
const numberOfDatasets = ref(0);
const autoHeight = ref(false);

const areaData = computed(() => {
  let data = [];
  for (let index = 0; index < numberOfDatasets.value; index++) {
    let gd = {};
    groups.value.forEach((group, i) => {
      gd[group] = Math.floor(Math.random() * 300);
    });
    gd.name = `Dataset ${index + 1}`;
    data.push(gd);
  }

  return data;
});

// const areaData = ref([
// {
//   name: "Jan",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Feb",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Mar",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Apr",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "May",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Jun",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Jul",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Aug",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Sep",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// {
//   name: "Oct",
//   total: Math.floor(Math.random() * 300),
//   prediction: Math.floor(Math.random() * 300),
//   change: Math.floor(Math.random() * 300),
// },
// ]);

const addRandomData = () => {
  numberOfDatasets.value++;
};

const removeRandomData = () => {
  numberOfDatasets.value--;
};

const addGroup = () => {
  groups.value.push(`Group ${groups.value.length + 1}`);
};

const removeGroup = () => {
  groups.value.pop();
};

const switchChart = () => {
  if (chartVisible.value) {
    autoHeight.value = false;
    chartVisible.value = false;
  } else {
    chartVisible.value = true;
    setTimeout(() => {
      autoHeight.value = true;
    }, 300);
  }
};

const data = ref([
  { x: 0, y: 0 },
  { x: 1, y: 2 },
  { x: 2, y: 1 },
]);
</script>

<style scoped>
.screen-template {
  grid-template-rows: 1fr 1fr;
}

.chart {
  height: 210px;
}

.auto-height {
  height: 100%;
}
</style>
