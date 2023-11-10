# Serverless API with Vercel

## Authors
Jacob Bassett

## Dates
11-8-2023

## Version
1.0.0.0

## Description
This is a practice project to become comfortable with crud operations in Python and deploy this functionality to Vercel.

## RUN

    1. Search by country to discover capital city(ies).
            Address Bar: <https://capital-finder-sand.vercel.app/api/capital-finder?country=south%20africa>
            Response: "The capitals of South Africa are Pretoria, Bloemfontein, and Cape Town."
    2. Search by capital to discover country. 
            Address Bar: <https://capital-finder-sand.vercel.app/api/capital-finder?capital=paris>
            Response: "Paris is the capital of France."
    3. Find additional information about a country by adding 'languages' and/or 'currencies' query parameters. 
            Address Bar: <https://capital-finder-sand.vercel.app/api/capital-finder?country=south%20africa&languages=true&currencies=true>
            Response: The capitals of South Africa are Pretoria, Bloemfontein, and Cape Town. People in South Africa might speak Afrikaans, English, Southern Ndebele, Northern Sotho, Southern Sotho, Swazi, Tswana, Tsonga, Venda, Xhosa, or Zulu. People in South Africa might pay with the South African Rand.
    4. Test your knowledge, discovery if a city is the capital of a country.
            Address Bar: <https://capital-finder-sand.vercel.app/api/capital-finder?country=canada&languages=true&currencies=true&capital=ottawa>
            Response: True, Ottawa is the capital of Canada.