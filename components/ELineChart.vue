<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script setup>
import { registerTheme, graphic } from "echarts";
import { use } from "echarts/core";

import { SVGRenderer, CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import dark from "../assets/themes/dark.json";
import { TooltipComponent, LegendComponent } from "echarts/components";
import VChart, { THEME_KEY, INIT_OPTIONS_KEY } from "vue-echarts";

const props = defineProps({
  data: Array,
  chartPadding: {
    type: Object,
    default: {
      top: 0,
      left: 0,
      right: 0,
      bottom: 50,
    },
  },
  showLegend: {
    type: Boolean,
    default: true,
  },
  showYAxis: {
    type: Boolean,
    default: false,
  },
  zeroBoundaryGap: {
    type: Boolean,
    default: false,
  },
  area: {
    type: Boolean,
    default: false,
  },
});

use([SVGRenderer, CanvasRenderer, PieChart, TooltipComponent, LegendComponent]);
registerTheme("dark", dark);
provide(THEME_KEY, "dark");

provide(INIT_OPTIONS_KEY, {
  renderer: "svg",
});

const option = computed(() => {
  return {
    xAxis: {
      type: "category",
      data: xAxis.value,
      show: true,
      boundaryGap: !props.zeroBoundaryGap,

      axisTick: {
        show: false,
      },
      axisLabel: {
        show: true,
        inside: false,
      },
      splitLine: {
        show: false,
      },
    },
    yAxis: {
      type: "value",
      show: true,
      axisTick: {
        show: true,
      },
      axisLine: {
        show: false,
      },
      axisLabel: {
        show: props.showYAxis,
        inside: props.showYAxis,
      },
    },

    legend: {
      show: props.showLegend,
      data: seriesNames.value,
      orient: "horizontal",
      bottom: 0,
      inactiveColor: "#1b1b1b",
      itemStyle: {
        borderCap: "square",
      },
      lineStyle: {
        width: 0,
        inactiveWidth: 0,
        inactiveColor: "#1b1b1b",
      },
    },

    series: computedSeries.value,
    grid: {
      show: false,

      ...props.chartPadding,
    },
  };
});

const computedSeries = computed(() => {
  return seriesNames.value.map((name, index) => {
    return {
      name,
      data: props.data.map((item) => item[name]),
      type: "line",
      smooth: true,
      areaStyle: props.area
        ? {
            color: new graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: dark.color[index] + "ff",
              },
              {
                offset: 1,
                color: dark.color[index] + "10",
              },
            ]),
          }
        : null,

      emphasis: {
        focus: "series",
      },
      stack: props.area ? "Total" : null,
    };
  });
});

const xAxis = computed(() => {
  return props.data.map((item, index) => {
    return props.zeroBoundaryGap &&
      (index == 0 || index == props.data.length - 1)
      ? ""
      : item.name;
  });
});

const seriesNames = computed(() => {
  return Object.keys(props.data[0]).filter((key) => key !== "name");
});

console.log(props.config);
</script>

<style>
.toolip {
  @apply !bg-background !border-muted !rounded-md !shadow-lg;
}
</style>
