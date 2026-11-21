# -*- coding: utf-8 -*-
html_path = "/home/sabrisatharamanathan/my-project/Aram-Karma/Karma-WorkshopActivities.html"

content = """
            <!-- ========================================================= -->
            <!-- 5. VALLALAR'S 44 CONFESSIONS & PROHIBITIONS HUB -->
            <!-- ========================================================= -->
            <section class="section-block" id="vallalar-hub">
                <div class="section-header-title">
                    <i data-lucide="shield-alert" style="color:#ef4444;"></i>
                    வள்ளலாரின் மனுமுறை கண்ட வாசகம்: 44 பாவங்களின் முழுமையான ஆய்வு மையம்
                </div>
                <div class="section-header-subtitle">
                    இராமலிங்க வள்ளலார் அவர்கள், மனிதர்கள் அறியாமல் என்னவெல்லாம் பாவங்கள் செய்ய முடியும் என்பதைத் தனது 'மனுமுறை கண்ட வாசகத்தில்' நெஞ்சை உலுக்கும் வகையில் பட்டியலிடுகிறார். எவை எவை பாவம் என்று தெரிந்தால்தான் அவற்றை நாம் தீவிர வைராக்கியத்துடன் தவிர்க்க முடியும்!
                </div>

                <!-- Filter Buttons -->
                <div class="vallalar-filter-bar">
                    <button class="btn-v-filter active" onclick="filterVallalar('all', this)">அனைத்தும் (All 44)</button>
                    <button class="btn-v-filter" onclick="filterVallalar('society', this)">1. சமூகம் &amp; நீதி (Society &amp; Justice)</button>
                    <button class="btn-v-filter" onclick="filterVallalar('poor', this)">2. ஏழை &amp; பசியுள்ளோர் (Poor &amp; Hungry)</button>
                    <button class="btn-v-filter" onclick="filterVallalar('nature', this)">3. இயற்கை &amp; உயிரினங்கள் (Nature &amp; Animals)</button>
                    <button class="btn-v-filter" onclick="filterVallalar('family', this)">4. பெண்மை &amp; குடும்பம் (Women &amp; Family)</button>
                    <button class="btn-v-filter" onclick="filterVallalar('spiritual', this)">5. குரு &amp; தெய்வம் (Guru &amp; Divine)</button>
                </div>

                <!-- Search Input -->
                <div class="vallalar-search-box">
                    <i data-lucide="search" class="vallalar-search-icon" style="width:18px; height:18px;"></i>
                    <input type="text" id="vallalar-search" class="vallalar-search-input" placeholder="வள்ளலாரின் பாவப் பட்டியலில் தேடுக (எ.கா: பசி, மரம், குளம், குரு, நட்பு, நெல்)..." onkeyup="searchVallalar()">
                </div>

                <!-- Vallalar Interactive Table -->
                <div class="vallalar-table-wrap">
                    <table class="vallalar-table" id="vallalar-table">
                        <thead>
                            <tr>
                                <th style="width:60px;">எண்</th>
                                <th style="width:340px;">வள்ளலாரின் மூல வாசகம் (பாடல் வரி)</th>
                                <th>பொருள் &amp; நவீன வாழ்வில் இதன் வடிவம்</th>
                                <th style="width:160px;">தவிர்க்கும் வைராக்கியம்</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Category 1: Society & Justice -->
                            <tr data-cat="society">
                                <td>1</td>
                                <td><strong>நல்லோர் மனத்தை நடுங்கச் செய்தேனோ!</strong></td>
                                <td>சான்றோர்களையும் நற்குணமுடையோரையும் அச்சுறுத்தி பயமுறுத்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>2</td>
                                <td><strong>வலிய வழக்கிட்டு மானங் கெடுத்தேனோ!</strong></td>
                                <td>காரணமின்றி வலிந்து வழக்குப் போட்டு பிறரின் மானத்தை பொதுவில் பறித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>3</td>
                                <td><strong>தானங் கொடுப்போரைத் தடுத்து நின்றேனோ!</strong></td>
                                <td>ஒருவர் நற்காரியங்களுக்கு தானம் செய்வதைத் தடுத்து நிறுத்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>4</td>
                                <td><strong>கலந்த சிநேகரைக்கலகஞ் செய்தேனோ!</strong></td>
                                <td>ஒற்றுமையாக இணைந்திருக்கும் நண்பர்களிடையே குழப்பம் விளைவித்து பிரித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>5</td>
                                <td><strong>மனமொத்த நட்புக்கு வஞ்சகஞ் செய்தேனோ!</strong></td>
                                <td>உளப்பூர்வமாக நம்பிய நண்பனுக்கு முதுகில் குத்தி வஞ்சகம் செய்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>6</td>
                                <td><strong>குடிவரி யுயர்த்திக் கொள்ளை கொண்டேனோ!</strong></td>
                                <td>அதிகார பலத்தால் அதிகப்படியான வரிகளைத் திணித்து மக்களைக் கொள்ளையடித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>7</td>
                                <td><strong>தருமம் பாராது தண்டஞ் செய்தேனோ!</strong></td>
                                <td>அறநெறியையும் நீதியையும் ஆராயாமல் அப்பாவி மக்களுக்கு தண்டனை விதித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>8</td>
                                <td><strong>மண்ணோரம் பேசி வாழ்வழித்தேனோ!</strong></td>
                                <td>நிலத்தின் எல்லைப் பிரச்சினையில் ஒருதலைப்பட்சமாகப் பேசி அடுத்தவர் வாழ்வை அழித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>9</td>
                                <td><strong>களவு செய்வோர்க்கு உளவு சொன்னேனோ!</strong></td>
                                <td>திருடர்களுக்கும் குற்றவாளிகளுக்கும் உடந்தையாக இருந்து உளவு தகவல்களைக் கூறுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>10</td>
                                <td><strong>பொருளை இச்சித்துப் பொய் சொன்னேனோ!</strong></td>
                                <td>அடுத்தவர் செல்வத்தின் மீது கொண்ட பேராசையினால் பொய் பேசி ஏமாற்றுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>11</td>
                                <td><strong>ஆசைகாட்டி மோசஞ் செய்தேனோ!</strong></td>
                                <td>போலி வாக்குறுதிகளை அள்ளிவீசி பேராசையைத் தூண்டி மோசடி செய்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>12</td>
                                <td><strong>வரவுபோக்கு ஒழிய வழியடைத்தேனோ!</strong></td>
                                <td>பொதுமக்கள் சென்றுவரும் பொதுப் பாதைகளையும் நடைவழிகளையும் ஆக்கிரமித்து அடைத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>13</td>
                                <td><strong>கல்லும் நெல்லும் கலந்து விற்றேனோ!</strong></td>
                                <td>லாப வெறியினால் உணவுப் பொருட்களில் கலப்படம் செய்து விற்று மக்களின் உயிரைப் பறித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>14</td>
                                <td><strong>அன்புடையவர்க்குத் துன்பஞ் செய்தேனோ!</strong></td>
                                <td>நம்மிடம் மெய்யன்பும் பாசமும் கொண்டவர்களுக்கு வேதனையையும் துன்பத்தையும் தருதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="society">
                                <td>15</td>
                                <td><strong>கலங்கி பயாளித்தோரைக் காட்டிக்கொடுத்தேனோ!</strong></td>
                                <td>பயந்து அடைக்கலம் தேடி ஒளிந்திருப்பவர்களை எதிரிகளிடம் காட்டிக் கொடுத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>

                            <!-- Category 2: Poor & Hungry -->
                            <tr data-cat="poor">
                                <td>16</td>
                                <td><strong>ஏழைகள் வயிறு எரியச் செய்தேனோ!</strong></td>
                                <td>ஆதரவற்ற ஏழைகளின் வயிற்றில் அடித்து அவர்களைப் பசியிலும் கண்ணீரிலும் ஆழ்த்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="poor">
                                <td>17</td>
                                <td><strong>வேலையிட்டுக் கூலி குறைத்தேனோ!</strong></td>
                                <td>உழைப்பாளிகளை கசக்கிப் பிழிந்துவிட்டு அவர்களின் வியர்வைக்குரிய நியாயமான கூலியைக் குறைத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="poor">
                                <td>18</td>
                                <td><strong>பசித்தோர் முகத்தைப் பாராதிருந்தேனோ!</strong></td>
                                <td>பசியோடு வந்து வாசலில் நிற்போரின் வாடிய முகத்தைப் பாராமல் உதாசீனப்படுத்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="poor">
                                <td>19</td>
                                <td><strong>இரப்போர்க்குப் பிச்சை இல்லையென்றேனோ!</strong></td>
                                <td>வீடு தேடி வந்து பிச்சை கேட்கும் வறியவர்களுக்கு இருந்தும் 'இல்லை' என்று விரட்டுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>

                            <!-- Category 3: Nature & Animals -->
                            <tr data-cat="nature">
                                <td>20</td>
                                <td><strong>உயிர்க்கொலை செய்வோர்க்க உபகாரஞ் செய்தேனோ!</strong></td>
                                <td>வாயில்லா பிராணிகளையும் ஜீவன்களையும் வதைத்துக் கொல்வோருக்கு உதவி செய்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>21</td>
                                <td><strong>பக்ஷியைக் கூண்டில் பதைக்க அடைத்தேனோ!</strong></td>
                                <td>வானில் சுதந்திரமாகப் பறக்கும் பறவைகளைப் பிடித்து கூண்டில் அடைத்து வேதனைப்படுத்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>22</td>
                                <td><strong>கன்றுக்குப் பாலூட்டாது கட்டிவைத்தேனோ!</strong></td>
                                <td>தாய்ப் பசுவின் பாலை பசியோடிருக்கும் அதன் கன்றுக்கு ஊட்டவிடாமல் பேராசையினால் கட்டிவைத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>23</td>
                                <td><strong>ஊன்சுவை யுண்டு உடல் வளர்த்தேனோ!</strong></td>
                                <td>நாக்கின் சுவைக்காக பிற உயிர்களைக் கொன்று அவற்றின் மாமிசத்தை உண்டு உடலை வளர்த்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>24</td>
                                <td><strong>குடிக்கின்ற நீருள்ள குளந் தூர்த்தேனோ!</strong></td>
                                <td>மக்களும் பிராணிகளும் குடிக்கும் நன்னீர் குளத்தை குப்பையைக் கொட்டி பாழாக்குதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>25</td>
                                <td><strong>வெயிலுக் கொதுங்கும் விருக்ஷ மழித்தேனோ!</strong></td>
                                <td>கோடை வெயிலில் மக்கள் இளைப்பாறும் நிழல் தரும் ஆல, அரச மரங்களை வெட்டி அழித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>26</td>
                                <td><strong>பகைகொண்டு அயலோர் பயிரழித்தேனோ!</strong></td>
                                <td>அக்கம்பக்கத்தினர் மீதான பொறாமையால் அவர்கள் கஷ்டப்பட்டு விளைவித்த பயிர்களை அழித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="nature">
                                <td>27</td>
                                <td><strong>பொதுமண்டபத்தைப் போயிடித்தேனோ!</strong></td>
                                <td>பொதுமக்கள் தங்கி இளைப்பாறும் சத்திரங்கள், மண்டபங்களை இடித்து பாழாக்குதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>

                            <!-- Category 4: Women & Family -->
                            <tr data-cat="family">
                                <td>28</td>
                                <td><strong>கோள் சொல்லிக் குடும்பங் குலைத்தேனோ!</strong></td>
                                <td>புறம்பேசி, கோள் மூட்டி ஒற்றுமையான குடும்பத்திற்குள் பிளவையும் பகையையும் உருவாக்குதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="family">
                                <td>29</td>
                                <td><strong>நட்டாற்றிற் கையை நழுவவிட்டேனோ!</strong></td>
                                <td>ஆபத்து காலத்தில் உடன் நின்று காப்பாற்றுவதாக வாக்களித்துவிட்டு நடுவழியில் கையை விடுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="family">
                                <td>30</td>
                                <td><strong>கற்பழிந்தவளைக் கலந்திருந்தேனோ!</strong></td>
                                <td>ஒழுக்கக் கேடான வழிகளில் பெண்மையை இழிவுபடுத்தி சிற்றின்பத்தில் மூழ்குதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="family">
                                <td>31</td>
                                <td><strong>காவல் கொண்டிருந்த கன்னியை அழித்தேனோ!</strong></td>
                                <td>குடும்பக் காவலில் இருக்கும் பெண்களின் கற்பையும் பாதுகாப்பையும் சிதைத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="family">
                                <td>32</td>
                                <td><strong>கணவன்வழி நிற்போரைக் கற்பழித்தேனோ!</strong></td>
                                <td>கற்புநெறி தவறாது வாழும் இல்லத்தரசிகளை சீரழித்து துன்புறுத்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="family">
                                <td>33</td>
                                <td><strong>கருப்பமழித்துக் களித்திருந்தேனோ!</strong></td>
                                <td>கருவில் வளரும் குழந்தையை அழித்து (கருக்கலைப்பு) ஈவிரக்கமின்றி களிப்படைதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="family">
                                <td>34</td>
                                <td><strong>தந்தைதாய் மொழியைத் தள்ளி நடந்தேனோ!</strong></td>
                                <td>தாய் தந்தையரின் அனுபவமிக்க நல்லுரைகளையும் வழிகாட்டல்களையும் புறக்கணித்து நடத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>

                            <!-- Category 5: Spiritual, Guru & Divine -->
                            <tr data-cat="spiritual">
                                <td>35</td>
                                <td><strong>குருவை வணங்கக் கூசிநின்றேனோ!</strong></td>
                                <td>மெய்ஞ்ஞானம் போதித்த குருவின் பாதங்களை தலைவணங்க கர்வத்தால் கூசி நிற்றல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>36</td>
                                <td><strong>குருவின் காணிக்கை கொடுக்க மறந்தேனோ!</strong></td>
                                <td>கல்வியும் ஞானமும் தந்த ஆசானுக்குரிய நன்றிக் காணிக்கையை செலுத்த மறத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>37</td>
                                <td><strong>கற்றவர் தம்மைக் கடுகடுத்தேனோ!</strong></td>
                                <td>நூற்களைக் கற்றுணர்ந்த அறிஞர்களைப் பார்த்து பொறாமையுடன் கடுகடுத்துப் பேசுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>38</td>
                                <td><strong>பெரியோர் பாட்டிற் பிழைசொன்னேனோ!</strong></td>
                                <td>அருளாளர்கள் பாடிய தெய்வீகப் பாடல்களில் அகந்தையால் குதர்க்கமாக குற்றம் காணுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>39</td>
                                <td><strong>ஆலயக் கதவை அடைத்து வைத்தேனோ!</strong></td>
                                <td>பக்தர்கள் இறைவனைத் தரிசிக்க முடியாதபடி ஆலயக் கதவுகளை காரணமின்றி மூடிவைத்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>40</td>
                                <td><strong>சிவனடியாரைச் சீறி வைதேனோ!</strong></td>
                                <td>இறைவனின் மெய்யடியார்களைக் கோபத்தோடு சீறித் திட்டி அவமானப்படுத்துதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>41</td>
                                <td><strong>தவஞ் செய்வோரைத் தாழ்வு சொன்னேனோ!</strong></td>
                                <td>கடுந்தவம் செய்யும் ஆன்மீக சாதகர்களை இழிவாகப் பேசி பரிகசித்தல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>42</td>
                                <td><strong>சுத்த ஞானிகளைத் தூஷணஞ் செய்தேனோ!</strong></td>
                                <td>காமக்குரோதம் கடந்த பரிசுத்த ஞானிகளை அவதூறு பேசித் தூற்றுதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>43</td>
                                <td><strong>தெய்வ மிகழ்ந்து செருக்கடைந்தேனோ!</strong></td>
                                <td>இறைவனை இகழ்ந்து, எல்லாம் நானே செய்கிறேன் என்ற மமதையோடு செருக்கடைதல்.</td>
                                <td><span class="karma-badge b-nishiddha">விலக்குக</span></td>
                            </tr>
                            <tr data-cat="spiritual">
                                <td>44</td>
                                <td><strong>என்ன பாவம் செய்தேனோ! இன்னதென்றறியேனே!</strong></td>
                                <td>தெரிந்தோ தெரியாமலோ செய்த வினைகளை உணர்ந்து இறைவனிடம் சரணடைந்து மன்னிப்பு வேண்டுதல்.</td>
                                <td><span class="karma-badge b-prayaschitta">சரணாகதி</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- ========================================================= -->
            <!-- 6. 9 DAILY SACRED PRAYERS (NITYA PRARTHANA SHLOKA HUB) -->
            <!-- ========================================================= -->
            <section class="section-block" id="prayers-hub">
                <div class="section-header-title">
                    <i data-lucide="sparkles" style="color:var(--saffron-primary);"></i>
                    தினசரி சொல்ல வேண்டிய 9 நித்ய பிரார்த்தனை சுலோகங்கள் (Daily Shlokas)
                </div>
                <div class="section-header-subtitle">
                    ஸ்ரீ பாலசுந்தரம் அவர்கள் தொகுத்து வழங்கிய, விழிப்பிலிருந்து உறங்கும் வரை நாள்தோறும் சொல்ல வேண்டிய 9 தெய்வீக சுலோகங்களும், தமிழ் விளக்கங்களும்:
                </div>

                <div class="prayers-grid">
                    <!-- Shloka 1 -->
                    <div class="prayer-card" id="shloka-1">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">1. காலை துயிலெழும் போது</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-1-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">கரதர்சனம் (உள்ளங்கை தரிசனம்)</h4>
                            <div class="prayer-shloka-box" id="shloka-1-txt">
கராக்ரே வஸதே லக்ஷ்மீ கரமத்யே ஸரஸ்வதீ |<br>
கரமூலே ஸ்திதா கௌரி: ப்ரபாதே கரதர்சனம் ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> நமது விரல்களின் நுனியில் லக்ஷ்மி தேவியும், உள்ளங்கையின் மத்தியில் ஸரஸ்வதி தேவியும், உள்ளங்கையின் அடிப்பகுதியில் கௌரி (பார்வதி) தேவியும் வீற்றிருக்கிறார்கள். காலையில் கண்விழிக்கும் போது உள்ளங்கையைப் பார்த்து இவர்களைத் தரிசிப்பதன் மூலம் அன்றைய நாள் மங்களகரமாக விடியட்டும்!
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 2 -->
                    <div class="prayer-card" id="shloka-2">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">2. பூமியில் கால் வைக்கும் முன்</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-2-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">பூமி வந்தனம் (க்ஷமா பிரார்த்தனை)</h4>
                            <div class="prayer-shloka-box" id="shloka-2-txt">
ஸமுத்ர வஸனே தேவி பர்வத ஸ்தன மண்டலே |<br>
விஷ்ணு பத்னி நமஸ்துப்யம் பாத ஸ்பர்சம் க்ஷமஸ்வமே ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> சமுத்திரங்களை ஆடையாகவும், மலைகளைப் பால்சுரக்கும் மார்பகங்களாகவும் கொண்டு எங்கும் வியாபித்திருக்கும் விஷ்ணுவின் பத்தினியான பூமாதேவியே! உன்னை எனது கால்களால் தீண்டுவதற்கு என்னை மன்னித்தருள்வாயாக! பூமி நம்மைத் தாங்குவதால் மன்னிப்புக் கேட்கிறோம்.
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 3 -->
                    <div class="prayer-card" id="shloka-3">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">3. நீராடும் போது</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-3-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">புண்ணிய நதிகள் ஆவாகனம்</h4>
                            <div class="prayer-shloka-box" id="shloka-3-txt">
கங்கே ச யமுனே சைவ கோதாவரி ஸரஸ்வதீ |<br>
நர்மதே ஸிந்து காவேரீ ஜலேஸ்மின் சன்னிதிம் குரு ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> புனித நதிகளான கங்கை, யமுனை, கோதாவரி, சரஸ்வதி, நர்மதை, சிந்து, காவிரி ஆகிய புண்ணிய நதிகளே! நான் குளிக்கும் இந்த நீரில் பிரசன்னமாகி (தோன்றி) என்னை உடலாலும் மனதாலும் புனிதப்படுத்துங்கள்.
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 4 -->
                    <div class="prayer-card" id="shloka-4">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">4. குங்குமம் வைக்கும் போது</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-4-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">மங்கள கௌரி சுலோகம்</h4>
                            <div class="prayer-shloka-box" id="shloka-4-txt">
ஸர்வ மங்கள மாங்கல்யே சிவே ஸர்வார்த்த ஸாதிகே |<br>
ஸரண்யே த்ரயம்பகே கௌரி நாராயணி நமோஸ்துதே ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> எல்லா மங்களங்களுக்கும் நாயகியே! எல்லாவற்றையும் சாதித்துத் தருபவளே! முப்புரமும் எரித்த சிவபெருமானின் தேவியே! கௌரியே! நாராயணனின் சகோதரியே! உன்னை சரணடைந்து நமஸ்கரிக்கிறேன்.
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 5 -->
                    <div class="prayer-card" id="shloka-5">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">5. திருநீறு அணியும் போது</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-5-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">தேவாரத் திருநீற்றுப் பதிகம்</h4>
                            <div class="prayer-shloka-box" id="shloka-5-txt">
மந்திர மாவது நீறு வானவர் மேலது நீறு<br>
சுந்தர மாவது நீறு துதிக்கப் படுவது நீறு<br>
தந்திர மாவது நீறு சமயத்தி லுள்ளது நீறு<br>
செந்துவர் வாயுமை பங்கன் திருஆல வாயான் திருநீறே.
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> திருஞானசம்பந்தர் அருளிய தேவாரம்: செவ்வாய் உமையம்மையின் பங்கனும் மதுரை திருஆலவாயில் உறையும் சிவபெருமானின் திருநீறே மந்திரமாகவும், அழகாகவும், வழிபடத்தக்கதாகவும் விளங்கி நம்மை சகல வினைகளிலிருந்தும் காக்கிறது!
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 6 -->
                    <div class="prayer-card" id="shloka-6">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">6. கோபி / திருமண் இடும் போது</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-6-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">வாஸுதேவ கிருஷ்ண தியானம்</h4>
                            <div class="prayer-shloka-box" id="shloka-6-txt">
க்ருஷ்ணாய வாஸுதேவாய தேவகீ நந்தநாய ச |<br>
நந்தகோப குமாராய கோவிந்தாய நமோ நம: ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> வாசுதேவரின் மைந்தனும், தேவகியின் ஆனந்தமும், நந்தகோபனின் செல்லக் குழந்தையும், அனைத்து ஜீவன்களையும் ரட்சிக்கும் கோவிந்தனுமான ஸ்ரீ கிருஷ்ண பரமாத்மாவை மீண்டும் மீண்டும் வணங்குகிறேன்.
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 7 -->
                    <div class="prayer-card" id="shloka-7">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">7. திருவிளக்கு ஏற்றும் போது</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-7-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">தீபஜ்யோதி வணக்கம்</h4>
                            <div class="prayer-shloka-box" id="shloka-7-txt">
சுபம் கரோதி கல்யாணம் ஆரோக்யம் தன-ஸம்பதா |<br>
சத்ரு-புத்தி-விநாசாய தீபஜ்யோதிர்-நமோஸ்துதே ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> மங்களத்தையும், நற்பேற்றினையும், நீண்ட ஆயுளையும் ஆரோக்கியத்தையும், செல்வச் செழிப்பையும் தந்து, அறிவின் பகை ஆகிய அஞ்ஞானத்தை அகற்றும் மகா வல்லமை பொருந்திய தீப ஜோதியே! உன்னை பணிந்து வணங்குகிறேன்.
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 8 -->
                    <div class="prayer-card" id="shloka-8">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge">8. உணவு உண்ணும் முன்</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-8-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">அன்னபூரணி பிரார்த்தனை</h4>
                            <div class="prayer-shloka-box" id="shloka-8-txt">
அன்னபூர்ணே ஸதாபூர்ணே சங்கரப்ராணவல்லபே |<br>
ஞானவைராக்ய ஸித்யர்த்தம் பிக்ஷாம் தேஹி ச பார்வதீ ||
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> எப்போதுமே பரிபூரணமாய் நிறைந்திருக்கும் அன்னபூரணியே! சங்கரரின் உயிர்த் துணையே! பார்வதி தேவியே! எனக்கு உணவோடு சேர்த்து மெய்ஞ்ஞானமும் உலகப் பற்றற்ற வைராக்கியமும் கிடைப்பதற்காக உன்னிடம் பிச்சை கேட்கிறேன்.
                            </div>
                        </div>
                    </div>

                    <!-- Shloka 9 -->
                    <div class="prayer-card" id="shloka-9" style="border-color:#f59e0b;">
                        <div>
                            <div class="prayer-meta">
                                <span class="prayer-time-badge" style="background:#f59e0b; color:#000;">9. இரவில் உறங்கும் முன்</span>
                                <button class="btn-copy-shloka" onclick="copyShlokaText('shloka-9-txt')">
                                    <i data-lucide="copy" style="width:12px; height:12px;"></i> நகலெடு
                                </button>
                            </div>
                            <h4 style="font-size:1.1rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">பூரண சரணாகதி சமர்ப்பணம்</h4>
                            <div class="prayer-shloka-box" id="shloka-9-txt">
"உண்ணலும் உனதே! உயிர்த்தலும் உனதே!<br>
உடல், உயிர், மனம் எல்லாம் உனதே!<br>
எண்ணலும் உனதே! இச்சையும் உனதே!<br>
எண்செயல் பயனெல்லாம் உனதே!"
                            </div>
                            <div class="prayer-meaning">
                                <strong>பொருள்:</strong> ஸ்ரீ பாலசுந்தரம் அவர்கள் அருளியது: பகல் முழுவதும் செய்த செயல்களின் பயன்களையெல்லாம் இறைவனுக்கு அர்ப்பணித்து, தெரிந்தும் தெரியாமலும் செய்த தவறுகளுக்கு மன்னிப்புக் கேட்டு, முழுமையான சரணாகதி மனநிலையுடன் உறங்கச் செல்வது மிகச் சிறந்ததாகும்!
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

with open(html_path, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 5 written successfully.")
