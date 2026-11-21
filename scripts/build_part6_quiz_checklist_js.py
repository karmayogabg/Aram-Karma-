# -*- coding: utf-8 -*-
import shutil

html_path = "/home/sabrisatharamanathan/my-project/Aram-Karma/Karma-WorkshopActivities.html"
index_path = "/home/sabrisatharamanathan/my-project/Aram-Karma/index.html"

content = """
            <!-- ========================================================= -->
            <!-- 7. INTERACTIVE KARMA BALANCE SELF-AUDIT QUIZ -->
            <!-- ========================================================= -->
            <section class="section-block" id="quiz-hub">
                <div class="section-header-title">
                    <i data-lucide="help-circle" style="color:var(--saffron-primary);"></i>
                    கர்ம தராசு சுயமதிப்பீட்டு வினாடி வினா (Karma Self-Audit Quiz)
                </div>
                <div class="section-header-subtitle">
                    கீழே உள்ள 6 எளிய சூழ்நிலைக் கேள்விகளுக்கு உங்கள் உண்மை நிலையைத் தேர்வு செய்து, உங்கள் நடப்பு கர்ம தராசு எந்தப் பக்கம் சாய்கிறது என்பதை உடனடியாகக் கண்டறியுங்கள்:
                </div>

                <div class="quiz-card">
                    <form id="karma-quiz-form" onsubmit="calculateKarmaScore(event)">
                        <!-- Q1: Nitya Karma -->
                        <div class="quiz-q-block">
                            <div class="quiz-q-title">
                                <span>1.</span> காலையில் கண்விழிக்கும் போது உங்கள் வழக்கம் என்ன? (நித்ய கர்மா)
                            </div>
                            <div class="quiz-options">
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q1" value="3" required>
                                    உள்ளங்கையைப் பார்த்து (கரதர்சனம்) பூமித்தாயிடம் மன்னிப்புக் கேட்டு இறைவனை நினைத்து அமைதியாக எழுகிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q1" value="2">
                                    நேரம் கிடைக்கும்போது கடவுளை நினைப்பேன்; சில நாட்களில் அவசரமாக கிளம்பிவிடுவேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q1" value="1">
                                    கண்விழித்தவுடன் மொபைல் போனைப் பார்த்து டென்ஷனுடன் எழுகிறேன்.
                                </label>
                            </div>
                        </div>

                        <!-- Q2: Pancha Yagnas -->
                        <div class="quiz-q-block">
                            <div class="quiz-q-title">
                                <span>2.</span> பிற உயிர்களுக்கு உணவளிப்பது &amp; பெற்றோரை மதிப்பது குறித்து: (பஞ்ச யக்ஞங்கள்)
                            </div>
                            <div class="quiz-options">
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q2" value="3" required>
                                    தினமும் காக்கை/நாய்களுக்கு உணவிட்டு, பெற்றோரை வணங்கி ஆசி பெறுகிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q2" value="2">
                                    அமாவாசை அல்லது விசேஷ நாட்களில் மட்டும் முன்னோரை நினைத்து தானம் செய்கிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q2" value="1">
                                    இதற்கெல்லாம் நேரம் இருப்பதில்லை; என்னை மட்டுமே கவனித்துக் கொள்கிறேன்.
                                </label>
                            </div>
                        </div>

                        <!-- Q3: Naimittika Karma -->
                        <div class="quiz-q-block">
                            <div class="quiz-q-title">
                                <span>3.</span> விரதங்கள், விசேஷ பூஜைகள் &amp; குடும்ப சம்ஸ்காரங்களை அணுகும் முறை: (நைமித்திகம்)
                            </div>
                            <div class="quiz-options">
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q3" value="3" required>
                                    சஷ்டி, ஏகாதசி போன்ற விரதங்களையும், 16 சம்ஸ்கார விழுமியங்களையும் முறைப்படி சிரத்தையோடு அனுஷ்டிக்கிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q3" value="2">
                                    குடும்பத்தினர் வற்புறுத்தினால் மட்டும் சடங்குகளில் ஒப்புக்கு பங்கேற்கிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q3" value="1">
                                    இவை தேவையில்லாத பழமைவாதம் என்று புறக்கணிக்கிறேன்.
                                </label>
                            </div>
                        </div>

                        <!-- Q4: Kamya Karma -->
                        <div class="quiz-q-block">
                            <div class="quiz-q-title">
                                <span>4.</span> வாழ்க்கையில் பதவி, சொத்து, வெற்றி போன்ற ஆசைகளை அடையும் வழி: (காம்யம்)
                            </div>
                            <div class="quiz-options">
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q4" value="3" required>
                                    100% நேர்மையான முயற்சியுடன், இறைவனிடம் நல்வழி வேண்டி பிரார்த்தனை செய்து அடைகிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q4" value="2">
                                    வெற்றி பெற வேண்டும் என்பதற்காக குறுக்கு வழிகளை யோசித்ததுண்டு.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q4" value="1">
                                    அடுத்தவருக்கு தீங்கு நேர்ந்தாலும் பரவாயில்லை, எனக்கு வெற்றி மட்டுமே முக்கியம்.
                                </label>
                            </div>
                        </div>

                        <!-- Q5: Nishkamya Karma -->
                        <div class="quiz-q-block">
                            <div class="quiz-q-title">
                                <span>5.</span> சமூக நலன், நீர்நிலைகள் &amp; பொதுச் சேவை பற்றிய உங்கள் பங்கு: (நிஷ்காம்யம்)
                            </div>
                            <div class="quiz-options">
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q5" value="3" required>
                                    எந்தப் பெயரோ புகழோ எதிர்பாராமல் ஏழைகளுக்கு கல்வி, மரக்கன்றுகள் நடுதல், பொதுத்தொண்டு செய்கிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q5" value="2">
                                    நால்வர் பார்த்துப் பாராட்டுவார்கள் என்றால் மட்டுமே பொதுநலப் பணிகளில் ஈடுபடுகிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q5" value="1">
                                    சமூகம் எப்படியோ போகட்டும், எனக்கும் என் குடும்பத்திற்கும் எந்தப் பாதிப்பும் இல்லையென்றால் போதும்.
                                </label>
                            </div>
                        </div>

                        <!-- Q6: Nishiddha & Prayaschitta -->
                        <div class="quiz-q-block">
                            <div class="quiz-q-title">
                                <span>6.</span> வள்ளலார் சுட்டிக்காட்டிய தவறுகளைத் தவிர்ப்பதும் பரிகாரமும்: (நிஷித்த &amp; பிராயச்சித்தம்)
                            </div>
                            <div class="quiz-options">
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q6" value="3" required>
                                    அறிந்தும் அறியாமலும் தவறிழைத்தால், உடனே வருந்தி மன்னிப்புக் கேட்டு ஆக்கபூர்வ பரிகாரம் (மரம் நடுதல்/தானம்) செய்கிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q6" value="2">
                                    தவறு என்று தெரிந்தாலும் சில சூழ்நிலைகளில் நியாயப்படுத்திக் கொள்கிறேன்.
                                </label>
                                <label class="quiz-opt-label">
                                    <input type="radio" name="q6" value="1">
                                    நான் செய்வது எதுவுமே தவறில்லை என்ற அகந்தையுடன் வாழ்கிறேன்.
                                </label>
                            </div>
                        </div>

                        <div style="text-align:center; margin-top:24px;">
                            <button type="submit" class="btn-nav btn-nav-primary" style="padding:12px 28px; font-size:1rem;">
                                <i data-lucide="scale" style="width:18px; height:18px;"></i> எனது கர்ம தராசைக் கணக்கிடுக! (Calculate Score)
                            </button>
                        </div>
                    </form>

                    <!-- Quiz Result -->
                    <div class="quiz-result-box" id="quiz-result">
                        <h3 style="font-family:var(--font-heading); font-size:1.5rem; font-weight:800; color:var(--text-main); margin-bottom:8px;" id="result-title">
                            மதிப்பீட்டு முடிவு
                        </h3>
                        <div style="font-size:2.2rem; font-weight:900; color:var(--saffron-primary); margin:10px 0;" id="result-score">
                            0 / 18
                        </div>
                        <p style="font-size:1rem; color:var(--text-main); max-width:760px; margin:0 auto; line-height:1.7;" id="result-desc">
                            விளக்கம்
                        </p>
                    </div>
                </div>
            </section>

            <!-- ========================================================= -->
            <!-- 8. FACILITATOR MASTER EQUIPMENT & READINESS CHECKLIST -->
            <!-- ========================================================= -->
            <section class="section-block" id="facilitator-check">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px;">
                    <div>
                        <div class="section-header-title">
                            <i data-lucide="clipboard-check" style="color:#10b981;"></i>
                            பயிற்றுநர் உபகரணங்கள் &amp; சரிபார்ப்புப் பட்டியல் (Facilitator Checklist)
                        </div>
                        <div class="section-header-subtitle">
                            5 மணி நேரப் பயிற்சிப் பட்டறை தொடங்குவதற்கு முன் தேவையான அனைத்து உபகரணங்களையும் சரிபார்த்து டிக் செய்யவும்:
                        </div>
                    </div>
                    <button class="btn-nav" onclick="resetChecklist()" style="font-size:0.82rem;">
                        <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i> அனைத்து டிக் மீட்டமை (Clear All)
                    </button>
                </div>

                <div class="checklist-grid">
                    <!-- Activity 1 Checklist -->
                    <div class="checklist-card" style="border-top:4px solid #f59e0b;">
                        <h4><span class="karma-badge b-kamya">செயல்பாடு 1</span> வினைக் கணக்கு &amp; தராசு</h4>
                        <label class="check-item"><input type="checkbox" id="chk-1-1"> <span>கருப்பு, மஞ்சள், பச்சை வண்ணத் துணிப் பட்டைகள் / கயிறுகள்</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-1-2"> <span>சிறிய இருதட்டு தராசு அல்லது சமநிலை பலகை</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-1-3"> <span>20 கருப்பு மணிகள் (பாவம்) &amp; 20 வெள்ளை மணிகள் (புண்ணியம்)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-1-4"> <span>வினைக் கணக்கு அட்டை (Karmic Ledger Worksheet)</span></label>
                    </div>

                    <!-- Activity 2 Checklist -->
                    <div class="checklist-card" style="border-top:4px solid #10b981;">
                        <h4><span class="karma-badge b-nitya">செயல்பாடு 2</span> நித்ய சக்கரம் &amp; யக்ஞ நாணயங்கள்</h4>
                        <label class="check-item"><input type="checkbox" id="chk-2-1"> <span>24 மணி நேர நித்ய சக்கர வரைபடத் தாள்கள் (தலா 1)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-2-2"> <span>5 வண்ண யக்ஞ வில்லைகள் (ரிஷி, பித்ரு, தேவ, பூத, மனுஷ்ய)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-2-3"> <span>9 நித்ய சுலோக பாக்கெட் அட்டைகள் (Shloka Pocket Cards)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-2-4"> <span>எழுதுகோல்கள் மற்றும் வண்ணக் குறிப்பான்கள்</span></label>
                    </div>

                    <!-- Activity 3 Checklist -->
                    <div class="checklist-card" style="border-top:4px solid #3b82f6;">
                        <h4><span class="karma-badge b-naimittika">செயல்பாடு 3</span> 16 சம்ஸ்காரங்கள் &amp; விரதங்கள்</h4>
                        <label class="check-item"><input type="checkbox" id="chk-3-1"> <span>16 சம்ஸ்கார விரிவுரை அட்டைகள் (Samskara Flashcards)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-3-2"> <span>மனித வாழ்வு காலக்கோடு பலகை (Life Timeline Board)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-3-3"> <span>திதி விரத சவால் அட்டைகள் (சஷ்டி, கிருத்திகை, ஏகாதசி போன்றவை)</span></label>
                    </div>

                    <!-- Activity 4 Checklist -->
                    <div class="checklist-card" style="border-top:4px solid #8b5cf6;">
                        <h4><span class="karma-badge b-nishkamya">செயல்பாடு 4</span> காம்யம் ➔ நிஷ்காம்யம் பாலம்</h4>
                        <label class="check-item"><input type="checkbox" id="chk-4-1"> <span>4 வகையான விருப்ப வழக்கு ஆய்வு அட்டைகள் (Case Studies)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-4-2"> <span>காம்யம் ➔ நிஷ்காம்யம் மாற்றப் படிவம் (Worksheets)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-4-3"> <span>குழு விளக்க சார்ட் பேப்பர்கள் மற்றும் மார்க்கர்கள்</span></label>
                    </div>

                    <!-- Activity 5 Checklist -->
                    <div class="checklist-card" style="border-top:4px solid #ef4444;">
                        <h4><span class="karma-badge b-nishiddha">செயல்பாடு 5</span> வள்ளலார் கண்ணாடி &amp; பசுமைப் பரிகாரம்</h4>
                        <label class="check-item"><input type="checkbox" id="chk-5-1"> <span>வள்ளலார் மனுமுறை 44 பாவங்கள் சுயஆய்வுப் படிவம்</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-5-2"> <span>பசுமைப் பரிகார உறுதி அட்டை (Green Restitution Card)</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-5-3"> <span>விதைப்பந்துகள் / மரக்கன்றுகள் உறுதிப் பதிவு புத்தகம்</span></label>
                    </div>

                    <!-- Activity 6 Checklist -->
                    <div class="checklist-card" style="border-top:4px solid var(--saffron-primary);">
                        <h4><span class="karma-badge" style="background:var(--saffron-glow); color:var(--saffron-primary);">செயல்பாடு 6</span> சங்கல்பம் &amp; மங்கள நிறைவு</h4>
                        <label class="check-item"><input type="checkbox" id="chk-6-1"> <span>அறம் காக்கும் ஷட் கர்ம சங்கல்ப வாசக அட்டை</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-6-2"> <span>குத்துவிளக்கு, மலர்கள், ஊதுபத்தி மற்றும் தீப ஆராதனை</span></label>
                        <label class="check-item"><input type="checkbox" id="chk-6-3"> <span>பயிற்சிப் பட்டறை நிறைவுச் சான்றிதழ்கள் (Certificates)</span></label>
                    </div>
                </div>
            </section>

        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p style="margin-bottom:8px; font-weight:800; font-size:1.05rem; color:var(--text-main);">
                அறம் — ஷட் கருமங்கள் பயிற்சிப் பட்டறை வழிகாட்டி (5-Hour Interactive Workshop Manual)
            </p>
            <p style="color:var(--text-muted); font-size:0.86rem; margin-bottom:12px;">
                அறம்வளர்த்தநாயகி சேவை மையம் • ஸ்ரீ பாலசுந்தரம் அவர்களின் அருளுரை தொகுப்பின் அடிப்படையில் வடிவமைக்கப்பட்டது.
            </p>
            <p style="color:var(--text-dim); font-size:0.78rem;">
                Created with Devotion &amp; Precision for Sanatana Dharma Trainers &amp; Volunteers • 2026 Edition
            </p>
        </div>
    </footer>

    <!-- Interactive JavaScript Logic -->
    <script>
        // Initialize Lucide Icons
        lucide.createIcons();

        // 1. Theme Toggle
        function toggleTheme() {
            const body = document.body;
            const isLight = body.classList.toggle('light-theme');
            const icon = document.getElementById('theme-icon');
            const label = document.getElementById('theme-label');
            if (isLight) {
                if (label) label.innerText = 'Dark Mode';
                if (icon) icon.setAttribute('data-lucide', 'moon');
                localStorage.setItem('karma-theme', 'light');
            } else {
                if (label) label.innerText = 'Bright Theme';
                if (icon) icon.setAttribute('data-lucide', 'sun');
                localStorage.setItem('karma-theme', 'dark');
            }
            lucide.createIcons();
        }

        // Load saved theme
        if (localStorage.getItem('karma-theme') === 'light') {
            document.body.classList.add('light-theme');
            const icon = document.getElementById('theme-icon');
            const label = document.getElementById('theme-label');
            if (label) label.innerText = 'Dark Mode';
            if (icon) icon.setAttribute('data-lucide', 'moon');
        }

        // 2. Web Audio Synthesizer Chime for Timers
        function playChime() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
                osc.frequency.exponentialRampToValueAtTime(783.99, ctx.currentTime + 0.3); // G5
                osc.frequency.exponentialRampToValueAtTime(1046.50, ctx.currentTime + 0.6); // C6
                gain.gain.setValueAtTime(0.3, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 1.2);
            } catch (e) {
                console.log('Audio not supported or permitted');
            }
        }

        // 3. Countdown Timers State & Handlers
        const timers = {};

        function formatTime(seconds) {
            const m = Math.floor(seconds / 60);
            const s = seconds % 60;
            return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
        }

        function startTimer(id, defaultDuration) {
            if (timers[id] && timers[id].interval) return;
            if (!timers[id]) {
                timers[id] = { remaining: defaultDuration, interval: null };
            }
            timers[id].interval = setInterval(() => {
                if (timers[id].remaining > 0) {
                    timers[id].remaining--;
                    const el = document.getElementById(`display-${id}`);
                    if (el) el.innerText = formatTime(timers[id].remaining);
                } else {
                    clearInterval(timers[id].interval);
                    timers[id].interval = null;
                    playChime();
                    alert(`⏰ செயல்பாடு ${id} நேரம் நிறைவடைந்தது! (Activity ${id} Time Completed)`);
                }
            }, 1000);
        }

        function pauseTimer(id) {
            if (timers[id] && timers[id].interval) {
                clearInterval(timers[id].interval);
                timers[id].interval = null;
            }
        }

        function resetTimer(id, defaultDuration) {
            pauseTimer(id);
            timers[id] = { remaining: defaultDuration, interval: null };
            const el = document.getElementById(`display-${id}`);
            if (el) el.innerText = formatTime(defaultDuration);
        }

        // 4. Vallalar 44 Table Filtering & Real-time Search
        let currentVallalarCat = 'all';

        function filterVallalar(cat, btn) {
            currentVallalarCat = cat;
            const buttons = document.querySelectorAll('.btn-v-filter');
            buttons.forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            searchVallalar();
        }

        function searchVallalar() {
            const query = (document.getElementById('vallalar-search').value || '').toLowerCase().trim();
            const rows = document.querySelectorAll('#vallalar-table tbody tr');

            rows.forEach(row => {
                const cat = row.getAttribute('data-cat');
                const text = row.innerText.toLowerCase();
                const matchesCat = (currentVallalarCat === 'all' || cat === currentVallalarCat);
                const matchesQuery = (!query || text.includes(query));

                if (matchesCat && matchesQuery) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        }

        // 5. Clipboard Copy Functions
        function copyShlokaText(elementId) {
            const el = document.getElementById(elementId);
            if (!el) return;
            const text = el.innerText.trim();
            navigator.clipboard.writeText(text).then(() => {
                alert('சுலோகம் வெற்றிகரமாக நகலெடுக்கப்பட்டது!');
            }).catch(err => {
                console.error('Clipboard copy failed:', err);
            });
        }

        function copyPledgeText(elementId) {
            const el = document.getElementById(elementId);
            if (!el) return;
            const text = el.innerText.trim();
            navigator.clipboard.writeText(text).then(() => {
                alert('ஷட் கர்ம புனித சங்கல்ப வாசகம் நகலெடுக்கப்பட்டது!');
            }).catch(err => {
                console.error('Clipboard copy failed:', err);
            });
        }

        // 6. Checklist Persistence with LocalStorage
        const chkBoxes = document.querySelectorAll('.checklist-card input[type="checkbox"]');
        chkBoxes.forEach(chk => {
            const saved = localStorage.getItem(`karma-chk-${chk.id}`);
            if (saved === 'true') chk.checked = true;
            chk.addEventListener('change', () => {
                localStorage.setItem(`karma-chk-${chk.id}`, chk.checked);
            });
        });

        function resetChecklist() {
            if (confirm('அனைத்து சரிபார்ப்பு டிக் குறியீடுகளையும் மீட்டமைக்க வேண்டுமா?')) {
                chkBoxes.forEach(chk => {
                    chk.checked = false;
                    localStorage.removeItem(`karma-chk-${chk.id}`);
                });
            }
        }

        // 7. Karma Quiz Score Calculation
        function calculateKarmaScore(e) {
            e.preventDefault();
            const form = document.getElementById('karma-quiz-form');
            const formData = new FormData(form);
            let score = 0;
            let answered = 0;

            for (let i = 1; i <= 6; i++) {
                const val = formData.get(`q${i}`);
                if (val) {
                    score += parseInt(val, 10);
                    answered++;
                }
            }

            if (answered < 6) {
                alert('தயவுசெய்து அனைத்து 6 கேள்விகளுக்கும் விடையளிக்கவும்!');
                return;
            }

            const resultBox = document.getElementById('quiz-result');
            const scoreDisplay = document.getElementById('result-score');
            const descDisplay = document.getElementById('result-desc');
            const titleDisplay = document.getElementById('result-title');

            scoreDisplay.innerText = `${score} / 18 புள்ளிகள்`;
            resultBox.style.display = 'block';

            if (score >= 16) {
                titleDisplay.innerText = '🌟 உத்தம சநாதனி • புண்ணியப் பாதை (Divine Balance)';
                descDisplay.innerHTML = '<strong>அற்புதம்!</strong> உங்கள் தினசரி வாழ்க்கை ஷட் கருமங்களுடன் இயைந்து பெருமளவில் புண்ணியப் பாதையில் பயணிக்கிறது. நித்ய கர்மானுஷ்டானத்தையும் நிஷ்காம்ய சேவையையும் தொடர்ந்து உலகிற்கு வழிகாட்டியாகத் திகழுங்கள்!';
                resultBox.style.borderColor = '#10b981';
                resultBox.style.background = 'rgba(16, 185, 129, 0.12)';
            } else if (score >= 11) {
                titleDisplay.innerText = '⚖️ சாதக நிலை • சமநிலை மாற்றம் தேவை (Striving Seeker)';
                descDisplay.innerHTML = '<strong>நன்று!</strong> அடிப்படை தர்மங்களை அறிந்துள்ளீர்கள்; ஆனால் நித்ய கர்மாக்களையும் பஞ்ச யக்ஞங்களையும் அன்றாட வழக்கமாக மாற்ற வேண்டியுள்ளது. காம்ய ஆசைகளைக் குறைத்து நிஷ்காம்ய சேவையில் அதிக கவனம் செலுத்துங்கள்!';
                resultBox.style.borderColor = '#f59e0b';
                resultBox.style.background = 'rgba(245, 158, 11, 0.12)';
            } else {
                titleDisplay.innerText = '🚩 விழிப்புணர்வுத் தொடக்கம் • உடனடியாக சீரமைக்க (Awakening Stage)';
                descDisplay.innerHTML = '<strong>கவலை வேண்டாம்!</strong> இன்று தொடங்கும் இந்த 5 மணி நேரப் பயிற்சிப் பட்டறை உங்கள் வாழ்க்கையை முற்றிலுமாக மாற்றப்போகிறது. வள்ளலாரின் 44 பாவங்களைத் தவிர்த்து, காலை விழிப்பிலிருந்து இரவு சமர்ப்பணம் வரை சிறு நற்பழக்கங்களைத் இன்றே தொடங்குங்கள்!';
                resultBox.style.borderColor = '#ef4444';
                resultBox.style.background = 'rgba(239, 68, 68, 0.12)';
            }

            resultBox.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>
</html>
"""

with open(html_path, "a", encoding="utf-8") as f:
    f.write(content)

# Copy to index.html as well for seamless browsing
shutil.copyfile(html_path, index_path)

print("Part 6 & Full HTML Application built and synced to index.html successfully!")
