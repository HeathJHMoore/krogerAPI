API_Token_Endpoint = 'https://api.kroger.com/v1/connect/oauth2/token'
API_Product_Endpoint = 'https://api.kroger.com/v1/products/'
client_credentials = #my client id and client secret from Kroger
mySQLUsername = #username for my python-anywhere mySQL database
mySQLPassword = #password for my python-anywhere mySQL database
locationIds = [
  '02600567', #21st av Kroger
  '02600511', #2615 Franklin Pike
  '02600895', #2131 Abbott Martin Rd
  '02600502', #800 Monroe St
  '02600843', #4560 Harding Pike
  '02600547', #5705 Charlotte Pike
  '02600542', #61 E Thompson Ln
  '02600880', #711 Gallatin Ave
  '02600533', #3930 Clarksville Pike
]
productIds = [
  #toothpaste
  '0003700094631', #Crest Pro-Health Advanced Extra Deep Clean Smooth Mint Paste Fluoride Toothpaste
  '0003500051088', #Colgate Great Regular Flavor Toothpaste
  '0003500046385',  #Colgate Total Whitening Toothpaste
  '0003700090309',  #Crest Tartar Protection Toothpaste
  #paper_towels,
  '0001111003992', #Kroger Paper Towels
  '0001111003993', #Kroger®  Select-A-Sheet Big Paper Towels"
  '0001111081440', #Check This Out…™ Paper Towels
  '0003700074801', #Bounty Select-A-Size Double Roll Paper Towels
  '0003700076234', #Bounty Select-A-Size Roll Paper Towels
  '0003600049413', #Viva Multi-Surface Cloth Choose-A-Sheet Paper Towels White Big Rolls
  #toilet_paper,
  '0001111081586', #check this out…™ Bath Tissue
  '0001111078596', #Kroger® Home Sense® Soft & Strong Double Roll Bath Tissue
  '0003040079184', #Angel Soft Double Roll Bath Tissue
  '0005400047618', #Scott Comfort Plus Double Roll Bath Tissue
  '0003600047747', #Cottonelle Ultra Clean Care Mega Roll Bath Tissue
  #dish_soap,
  '0003700097305', #Dawn Ultra Original Scent Dishwashing Liquid
  '0003500045093', #Palmolive Ultra Strength Original Dish Liquid
  '0003500044678', #Ajax Triple Action Orange Dish Liquid
  '0001111086784', #check this out…™ Lemon Dishwashing Liquid
  #produce,
  '0001111091128', #Simple Truth Organic™ Baby Spinach
  '0000000094011', #Organic Banana
  '0001111091659', #Simple Truth Organic™ Baby Carrots
  '0001111091131', #Simple Truth Organic™ Baby Spring Mix
  '0001111091068', #Simple Truth Organic™ Grape Tomatoes
  '0001111091657', #Simple Truth Organic™ Whole Carrots
  '0001111069101', #Simple Truth Organic™ Gala Apples
  '0003338322101', #Blueberries
  '0001111002498', #Simple Truth Organic™ Sliced Baby Bella Mushrooms
  '0001111069106', #Simple Truth Organic™ Honeycrisp Apples
  '0000000094062', #Organic - Cucumber
  '0001111001921', #Simple Truth Organic™ Thyme"
  '0001111002497', #Simple Truth Organic™ Sliced White Mushrooms
  '0000000094225', #Organic - Avocados
  '0000000004225', #Avocado - Large
  '0000000004046', #Avocado - Small
  '0000000004060', #Broccoli
  '0000000003082', #Broccoli - Crowns
  '0000000004627', #Greens -  Kale
  '0001111018170', #Kroger®  Kale Bag
  '0001111091727', #Simple Truth Organic™ Baby Kale
  '0000000004663', #Onions - White
  '0001111091682', #Kroger® Yellow Onions
  '0000000004068', #Onions - Green
  '0000000004166', #Onion - Sweet - Yellow
  '0000000004693', #Pepper - Jalapeno
  '0000000003121', #Bell Pepper - Orange
  '0000000004065', #Bell Pepper - Green - Large
  '0000000004688', #Red Bell Pepper
  '0000000004689', #Bell Pepper - Yellow
  #milk,
  '0001111040601', #Kroger®  Vitamin D Whole Milk
  '0001111041600', #Kroger®  2% Reduced Fat Milk
  '0001111041660', #Kroger®  1% Lowfat Milk
  '0001111042315', #Kroger® Fat Free Skim Milk
  '0001111050573', #Kroger®  1% Low Fat Chocolate Milk
  '0001111042852', #Simple Truth Organic™ 2% Reduced Fat Milk
  '0001111042854', #Simple Truth Organic™ 1% Low Fat Milk
  '0001111042850', #Simple Truth Organic™ Whole Milk
  '0002529300149', #Silk Unsweetened Almond Milk
  '0002529300136', #Silk Unsweetened Vanilla Almond Milk
  '0004157005670', #Blue Diamond Original Unsweetened Almond Milk
  '0004157005618', #Blue Diamond Almond Breeze Unsweetened Vanilla Almond Milk
  #yogurt,
  '0007047000300', #Yoplait Original Strawberry Yogurt
  '0007047000323', #Yoplait Original French Vanilla Yogurt
  '0007047000313', #Yoplait Original Strawberry Banana Low Fat Yogurt
  '0089470001006', #Chobani Peach on the Bottom Greek Yogurt
  '0081829001228', #Chobani Flip Almond Coco Loco Greek Yogurt
  '0089470001004', #Chobani Strawberry on the Bottom Greek Yogurt
  '0089470001016', #Chobani Black Cherry on the Bottom Greek Yogurt
  '0085392300210', #Noosa Lemon Yogurt
  '0085392300220', #Noosa Blueberry Yogurt
  '0003663203737', #Dannon Light & Fit Toasted Coconut Vanilla Greek Yogurt
  '0003663202601', #Dannon Activia Probiotic Yogurt Vanilla
  '0003663203733', #Dannon Light & Fit Vanilla Greek Yogurt
  #meat,
  '0001111097972', #Kroger® Ground Beef 80% Lean / 20% Fat
  '0001111096963', #Private Selection™ Angus Beef 90% Lean 10% Fat Ground Sirloin
  '0021065600000', #Heritage Farm™ Boneless & Skinless Chicken Breasts with Rib Meat
  '0021058100000', #Heritage Farm™  Boneless & Skinless Chicken Tenderloins (10-12 per Pack)
  '0061266931671', #Laura's Lean Beef All Natural 92% Lean Ground Beef
  '0023858840000', #"Salmon Atlantic Fillet (Fresh Farm Raised) (Service Counter)"
  '0073114951527', #Aqua Star Salmon Fillet
  '0001111077990', #Kroger® Wild Caught Boneless & Skinless Pink Salmon Fillets Family Size
  '0001111096419', #Private Selection™ Wild Alaskan Sockeye Applewood Smoked Salmon
  '0026947940000', #Shrimp Raw White X Large 21/25 Count (Farm Raised Previously Frozen) (Service Counter)
  '0026943940000', #Shrimp Cooked X Large 26/30 Count (Service Counter)
  '0001111096371', #Kroger® Crunchy Butterfly Shrimp
  '0001111096440', #Kroger Wild Caught Peeled & Deveined Medium Raw Shrimp
]
