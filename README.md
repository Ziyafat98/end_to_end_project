# Result
# ❓ Sual: Aylıq dəyişikliklər satışlara necə təsir göstərir?
Aylıq analiz göstərir ki, fevral ayında satışlarda azalma müşahidə olunmuşdur.
Mart ayından etibarən satışlar artım trendinə keçmiş, mart–may ayları satışların ən güclü olduğu dövr kimi seçilmişdir.
İyun ayında isə artım davam etsə də, daha stabil satış fazası müşahidə olunur.

# ❓ Sual: Günün hansı saatlarında satışlar daha yüksək olur?
Saatlıq analiz göstərir ki, satışlar səhər saatlarından başlayaraq 7–10 aralığında artım göstərir.
Ən yüksək satış isə saat 10-da qeydə alınmışdır.
Bu, günün ilk saatlarının satış baxımından daha aktiv olduğunu göstərir.

# ❓ Sual: Həftənin hansı günlərində satışlar daha yüksək olur?
## Nəticə / Insight:
- Həftə günü analizinə görə, satışlar **Monday və Friday** günləri daha yüksək olmuşdur.
- **Friday-də ən yüksək satış**: 101.7k
- Ən aşağı satış isə **Saturday** günündə qeydə alınmışdır.
Bu nəticələr göstərir ki, həftənin günləri satış performansına təsir göstərir və bəzi günlər daha aktiv olur.

# ❓ Sual: Say və gəlir baxımından məhsullar necə performans göstərir?

## Nəticə / Insight:
Top 5 məhsul həm satış, həm də gəlir baxımından liderdir: Barista Espresso (91,406.20), Brewed Chai tea (77,081.95, 26,250), Hot chocolate (72,416.00, 17,457), Gourmet brewed coffee (70,034.60, 25,973) və Brewed Black tea (47,932.00, 17,462). Ən çox satılan məhsul Brewed Chai tea həm satış, həm də gəlir baxımından top performans göstərir. Ən az gəlir gətirən məhsullar Green beans (1,340.00), Green tea (1,470.75), Organic Chocolate (1,679.60), Sugar free syrup (2,324.00) və Black tea (2,711.85) olaraq biznes üçün prioritet deyildir. Bu nəticələr göstərir ki, gəlir yalnız satış sayından asılı deyil, məhsulun qiyməti və satış strategiyası da rol oynayır.

# ❓ Sual: Məhsul kateqoriyaları satış və gəlir baxımından necə performans göstərir?

## Nəticə / Insight:
Ən çox satış və gəlir gətirən kateqoriyalar Coffee (269,952.45, 58,416) və Tea (196,405.95, 45,449) olaraq biznes üçün lider mövqedədir. Ən aşağı performans göstərən kateqoriyalar Flavours (8,408.80, 6,790) və Packaged Chocolate (4,407.64, 487) olub. Bu nəticə göstərir ki, **müştərilər əsasən Coffee və Tea kateqoriyasına üstünlük verir**, digər kateqoriyalar isə gəlir və satış baxımından daha az əhəmiyyətlidir.

# ❓ Sual: Aylara görə məhsul kateqoriyalarının satış performansı necədir?

## Nəticə / Insight:
Coffee və Tea kateqoriyaları bütün aylarda liderdir, yanvardan iyuna qədər Coffee (31,256 → 64,789) və Tea (22,621 → 46,243) kateqoriyaları satışını təxminən 2 dəfə artırıb. Bakery və Drinking Chocolate orta səviyyədə artım göstərir, Flavours və Packaged Chocolate isə ən aşağı performans göstərir və minimal gəlir gətirir. Bu nəticə göstərir ki, biznes üçün əsas prioritet kateqoriyalar Coffee və Tea-dir, digər kateqoriyalar isə ya marketinq dəstəyi ilə artırılmalı, ya da prioritetdən çıxarılmalıdır.

# ❓ Sual: Mağazalara görə satış performansı necədir?

## Nəticə / Insight:
Hell’s Kitchen (236,511.17, 71,737), Astoria (232,243.91, 70,991) və Lower Manhattan (230,057.25, 71,742) mağazaları satış və gəlir baxımından əsas mənbələrdir. Gəlir və satış sayı arasında fərqlilik müşahidə olunur: məsələn, Lower Manhattan ən çox məhsul satmasına baxmayaraq gəlir baxımından Hell’s Kitchen-i ötə bilmir. Bu nəticə göstərir ki, **mağaza lokasiyası, məhsul növü və qiymət strategiyası satış performansına birbaşa təsir göstərir.**

# ❓ Sual: Mağazalarda məhsul kateqoriyalarının satış performansı necədir?

## Nəticə / Insight:
Coffee və Tea bütün mağazalarda əsas gəlir mənbəyidir: Hell’s Kitchen (Coffee: 91,222.65, Tea: 64,701.30), Astoria (Coffee: 89,744.30, Tea: 67,839.90) və Lower Manhattan (Coffee: 88,985.50, Tea: 63,864.75). Bakery və Drinking Chocolate orta səviyyədə satış gətirir, Flavours və Packaged Chocolate isə bütün mağazalarda minimal performans göstərir. Bu nəticə göstərir ki, **mağazalarda kateqoriya strukturu oxşardır və biznes üçün prioritet kateqoriyalar Coffee və Tea-dir**, digər kateqoriyalar isə əlavə marketinq və strategiya dəstəyi tələb edə bilər.

# ❓ Sual: Hava şəraiti (orta temperatur) satışlara nə dərəcədə təsir göstərir?

## Nəticə / Insight:
Satışlar hava datası ilə birləşdirilərək Random Forest modeli qurulmuş və feature importance analizi aparılmışdır. Model nəticələrinə əsasən satışlara təsir edən əsas faktorlar ardıcıllıqla **month_num**, **day_num**, **temperature_2m_mean** və **store_id** olmuşdur. Vizualda açıq şəkildə görünür ki, **ay faktoru satışlara ən güclü təsiri göstərir**, gün faktoru ikinci yerdədir. Orta temperatur satışlara **müsbət, lakin mövsümi faktorlarla müqayisədə daha zəif təsir edir**. Bu nəticə göstərir ki, satışlar təkcə hava şəraitindən deyil, əsasən **mövsümi davranış və zaman faktorlarından** asılıdır, lakin temperatur satış proqnozlaşdırılmasında köməkçi dəyişən kimi dəyər yaradır.


