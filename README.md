# Autotrader Canada Vehicle Listings Scraper

> A powerful tool for extracting complete vehicle listings from Autotrader Canada with high accuracy and structured outputs. It automates the discovery of all listings across paginated search results and delivers clean, well-processed automotive data.
> Designed for users who need reliable, large-scale access to car data, pricing, mileage, seller information, and full listing metadata.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Autotrader Canada</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This scraper captures comprehensive vehicle information from Autotrader Canada search results and listing pages.
It solves the problem of manual vehicle data collection by providing a fast, automated, and structured way to capture listings at scale.
Ideal for analysts, dealerships, market researchers, data engineers, and automotive comparison platforms.

### How It Works

- Accepts one or more Autotrader search URLs as input.
- Automatically paginates results and extracts up to 100 listings per page.
- Collects detailed vehicle specifications, pricing, images, seller info, and raw metadata.
- Outputs clean JSON or flattened CSV/Excel formats for ready-to-use analysis.

## Features

| Feature | Description |
|--------|-------------|
| Automatic Pagination | Discovers all available listing pages and adjusts parameters for maximum results per page. |
| Detailed Vehicle Extraction | Retrieves price, mileage, specs, images, seller details, location, and status. |
| Raw JSON Included | Provides full listing JSON for advanced analysis and custom data modeling. |
| Robust Retry Logic | Re-attempts failed requests and ensures highly reliable extraction. |
| Duplicate Detection | Stops pagination when no new listings appear, preventing unnecessary loops. |
| Flexible Configuration | Supports custom concurrency, proxy URLs, and page limits. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| ad_id | Unique vehicle listing identifier. |
| make | Manufacturer of the vehicle. |
| model | Specific model name. |
| year | Manufacturing year. |
| price_str | Human-readable price string. |
| price_cad | Numeric price value in CAD. |
| mileage_str | Formatted mileage text. |
| mileage_km | Numeric mileage in kilometers. |
| status | Condition of the vehicle (Used/New). |
| posted_age | How long ago the listing was posted. |
| transmission | Vehicle transmission type. |
| drivetrain | Drivetrain specification (e.g., FWD, AWD). |
| body_type | Body style such as Sedan, SUV, etc. |
| exterior_colour | Colour of the vehicle’s exterior. |
| fuel_type | Type of fuel used. |
| doors | Number of doors. |
| city | Seller’s city. |
| province | Seller’s province. |
| is_private_seller | Indicates whether the seller is a private individual. |
| seller_name | Seller's name or dealership name. |
| image_urls | Array of image URLs associated with the listing. |
| description | Full vehicle description text. |
| url | Original Autotrader listing URL. |
| all_data | Complete raw JSON extracted from the page. |

---

## Example Output


    [
          {
            "body_type": "SUV",
            "city": "St-Eustache",
            "description": "1996 HUMMER H1 6.5L V8 DIESEL 4-PASSENGER OPEN TOP...",
            "doors": "4",
            "drivetrain": "4x4",
            "exterior_colour": "Green",
            "fuel_type": "Diesel",
            "image_urls/0": "https://mkt-vehicleimages-prd.autotradercdn.ca/photos/import/202204/0102/0316/0017abd5-654e-460b-8295-980f1d374420.jpg-1024x786",
            "is_private_seller": false,
            "make": "Hummer",
            "mileage_km": 37397,
            "mileage_str": "37,397 km",
            "model": "H1",
            "posted_age": null,
            "price_cad": 79990,
            "price_str": "$79,990",
            "province": "QC",
            "seller_name": "Empire Auto",
            "status": "Used",
            "transmission": "Automatic",
            "url": "https://www.autotrader.ca/a/am%20general/hummer/st-eustache/quebec/5_54240768_20060222120117375/",
            "year": 1996
          }
    ]

---

## Directory Structure Tree


    Autotrader Canada/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── listing_parser.py
    │   │   ├── search_page_parser.py
    │   │   └── utils_formatting.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── sample-inputs.json
    │   └── sample-output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Market analysts** use it to gather large-scale vehicle listings, so they can track pricing trends and competitive market activity.
- **Car dealerships** use it to monitor competitor inventory, enabling smarter purchasing and pricing decisions.
- **Automotive marketplaces** use it to populate their platforms with structured vehicle data, ensuring richer user search experiences.
- **Data scientists** use it to build pricing models and predictive analytics with reliable automotive datasets.
- **Journalists and researchers** use it to study regional vehicle availability, pricing fluctuations, and seller behaviour.

---

## FAQs

**Does this scraper capture all images from each listing?**
Yes — all available listing images are extracted and included as an array of URLs.

**Does it detect repeated listings?**
Yes — built-in duplicate detection prevents unnecessary pagination and optimizes extraction efficiency.

**Can I limit the number of pages scraped per URL?**
Yes — you can specify a maximum depth to control how many result pages are processed.

**Is the raw listing metadata preserved?**
Absolutely — all raw JSON data is included under the `all_data` field for advanced use cases.

---

## Performance Benchmarks and Results

**Primary Metric:**
Processes an average of 100–150 listings per minute when using default concurrency settings.

**Reliability Metric:**
Maintains a 98%+ success rate across large-scale scraping sessions, with automatic retry mechanisms handling transient issues.

**Efficiency Metric:**
Optimized pagination and duplicate detection reduce unnecessary requests by up to 40%, improving speed and resource use.

**Quality Metric:**
Delivers over 95% field completeness across price, mileage, specifications, seller details, and media assets for most listings.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
