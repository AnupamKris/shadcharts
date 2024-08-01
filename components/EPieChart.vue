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
  console.log(params);
  let template = `<div class="tooltip">`;
  template += `
    <div class="tooltip-item">
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
    className: "toolip",
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

<style>
.toolip {
  @apply !bg-background !border-muted !rounded-md !shadow-lg;
}

.tooltip-title {
  @apply font-bold text-foreground border-b p-3;
}

.tooltip-items {
  @apply flex flex-col gap-2 p-3;
}

.tooltip-item {
  @apply flex gap-2 items-center align-middle px-2;
}

.tooltip-item-color {
  @apply w-2.5 h-2.5 mr-2 rounded-full min-w-2.5 min-h-2.5;
}

.tooltip-item-name {
  @apply text-foreground;
}

.tooltip-item-value {
  @apply text-foreground text-right min-w-fit;
}
</style>
