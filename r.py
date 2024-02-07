import azure.ai.vision as vision

service_options = sdk.VisionServiceOptions(os.environ["VISION_ENDPOINT"],
                                           os.environ["VISION_KEY"])

image_source = sdk.VisionSource(url="<url>")

options = sdk.ImageAnalysisOptions()

options.features = (
    sdk.ImageAnalysisFeature.CAPTION |
    sdk.ImageAnalysisFeature.TEXT
)

options.language = "en"
options.gender_neutral_caption = True

image_analyzer = sdk.ImageAnalyzer(service_options, image_source, options)

result = image_analyzer.analyze()