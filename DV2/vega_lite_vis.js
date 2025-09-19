var vg_1 = "life_expectancy_map.vg.json";

vegaEmbed("#choropleth_map", vg_1)
    .then(function (result) {
        console.log("Choropleth map loaded successfully");
    })
    .catch(function (error) {
        console.error("Error loading the choropleth map:", error);
    });