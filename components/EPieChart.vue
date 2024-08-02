<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script setup>
import { registerTheme } from "echarts";
import { use } from "echarts/core";
import { SVGRenderer, CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import dark from "../assets/themes/dark.json";
import { TooltipComponent, LegendComponent } from "echarts/components";
import VChart, { THEME_KEY, INIT_OPTIONS_KEY } from "vue-echarts";

const props = defineProps({
  data: Array,
  config: {
    type: Object,
    default: {
      innerRadius: 50,
      outerRadius: 80,
    },
  },
});

use([SVGRenderer, CanvasRenderer, PieChart, TooltipComponent, LegendComponent]);
registerTheme("dark", dark);
provide(THEME_KEY, "dark");

provide(INIT_OPTIONS_KEY, {
  renderer: "svg",
});

const createTooltipMarkup = (params) => {
  const { seriesName, percent, color } = params;
  let template = `<div class="tooltip">`;
  template += `
    <div class="tooltip-item-pie">
      <div class="tooltip-item-color" style="background-color: ${color}"></div>
      <div class="tooltip-item-name">${seriesName}</div>
      <div class="tooltip-item-value ">${percent}%</div>
    </div>
    `;

  template += `</div>`;

  return template;
};

const option = ref({
  tooltip: {
    trigger: "item",
    className: "tooltip",
    formatter: createTooltipMarkup,
  },
  series: [
    {
      name: "Traffic Sources",
      type: "pie",
      radius: [props.config.innerRadius + "%", props.config.outerRadius + "%"],
      center: ["50%", "50%"],
      data: props.data,
      label: {
        show: false,
      },
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: "rgba(0, 0, 0, 0.5)",
        },
      },
    },
  ],
});
</script>

<style scoped></style>
