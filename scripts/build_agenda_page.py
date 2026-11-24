import json
import os

def main():
    with open('scripts/rishis_data.json', 'r', encoding='utf-8') as f:
        rishis_list = json.load(f)

    rishis_json_str = json.dumps(rishis_list, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>5 மணி நேர முழுமையான செயல்திட்டம் & நேரடிப் போதனை வழிகாட்டி — அறம் ஷட் கருமங்கள்</title>
    <meta name="description" content="கர்மா முதல் நிஷ்காமியம் வரை: 5 மணி நேர ஆன்மீகப் பரிணாமப் பாதை. செயல், கர்ம பந்தம், ஷட் கருமங்கள், பஞ்ச மகா யக்ஞங்கள், 200 ரிஷிகள் பட்டியல், நேரடி குழுச் செயல்பாடுகள் மற்றும் ஆசிரியர் வழிகாட்டி.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Mukta+Malar:wght@400;500;600;700;800&family=Noto+Sans+Tamil:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        :root {{
            --bg-base: #07090e;
            --bg-surface: #0f141f;
            --bg-card: #141c2c;
            --bg-card-hover: #1b263b;
            --border-color: rgba(255, 255, 255, 0.12);
            --border-focus: #f59e0b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            
            --saffron-primary: #f59e0b;
            --saffron-hover: #d97706;
            --saffron-glow: rgba(245, 158, 11, 0.28);
            
            --karma-nitya: #10b981;
            --karma-nitya-bg: rgba(16, 185, 129, 0.12);
            --karma-naimittika: #3b82f6;
            --karma-naimittika-bg: rgba(59, 130, 246, 0.12);
            --karma-kamya: #f59e0b;
            --karma-kamya-bg: rgba(245, 158, 11, 0.12);
            --karma-nishkamya: #8b5cf6;
            --karma-nishkamya-bg: rgba(139, 92, 246, 0.12);
            --karma-prayaschitta: #06b6d4;
            --karma-prayaschitta-bg: rgba(6, 182, 212, 0.12);
            --karma-nishiddha: #ef4444;
            --karma-nishiddha-bg: rgba(239, 68, 68, 0.12);
            
            --font-heading: 'Outfit', 'Cinzel', 'Noto Sans Tamil', sans-serif;
            --font-tamil: 'Noto Sans Tamil', 'Mukta Malar', sans-serif;
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --shadow-md: 0 10px 30px rgba(0,0,0,0.4);
            --shadow-lg: 0 16px 40px rgba(0,0,0,0.6);
        }}

        body.light-theme {{
            --bg-base: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #f1f5f9;
            --bg-card-hover: #e2e8f0;
            --border-color: rgba(0, 0, 0, 0.12);
            --text-main: #0f172a;
            --text-muted: #334155;
            --text-dim: #64748b;
            --saffron-glow: rgba(217, 119, 6, 0.15);
            --karma-nitya-bg: #ecfdf5;
            --karma-naimittika-bg: #eff6ff;
            --karma-kamya-bg: #fffbeb;
            --karma-nishkamya-bg: #f5f3ff;
            --karma-prayaschitta-bg: #ecfeff;
            --karma-nishiddha-bg: #fef2f2;
            --shadow-md: 0 8px 24px rgba(0,0,0,0.06);
            --shadow-lg: 0 16px 36px rgba(0,0,0,0.09);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: var(--font-tamil);
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.75;
            -webkit-font-smoothing: antialiased;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}

        .container {{
            max-width: 1320px;
            margin: 0 auto;
            padding: 0 24px;
        }}

        /* Navbar */
        .navbar {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(15, 20, 31, 0.94);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-color);
            padding: 12px 0;
            transition: all 0.3s ease;
        }}
        body.light-theme .navbar {{
            background: rgba(255, 255, 255, 0.95);
        }}
        .navbar-inner {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--text-main);
        }}
        .brand-logo {{
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: linear-gradient(135deg, #f59e0b, #b45309);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            box-shadow: 0 4px 16px var(--saffron-glow);
            font-size: 1.4rem;
        }}
        .brand-text h1 {{
            font-family: var(--font-heading);
            font-size: 1.15rem;
            font-weight: 800;
            line-height: 1.25;
            color: var(--text-main);
        }}
        .brand-text p {{
            font-size: 0.78rem;
            color: var(--saffron-primary);
            font-weight: 700;
            letter-spacing: 0.5px;
        }}

        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .btn-nav {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            font-size: 0.85rem;
            font-weight: 700;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid var(--border-color);
            background: var(--bg-surface);
            color: var(--text-main);
        }}
        .btn-nav:hover {{
            border-color: var(--saffron-primary);
            color: var(--saffron-primary);
            transform: translateY(-1px);
        }}
        .btn-nav-primary {{
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #000;
            border-color: var(--saffron-primary);
            font-weight: 800;
        }}
        .btn-nav-primary:hover {{
            background: #d97706;
            color: #000;
            box-shadow: 0 4px 14px var(--saffron-glow);
        }}

        /* Hero Banner */
        .hero {{
            padding: 44px 0 28px 0;
            text-align: center;
            background: radial-gradient(circle at 50% 15%, rgba(245, 158, 11, 0.16), transparent 70%);
            border-bottom: 1px solid var(--border-color);
            position: relative;
        }}
        .hero-badge-wrap {{
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 16px;
        }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(245, 158, 11, 0.14);
            border: 1px solid rgba(245, 158, 11, 0.4);
            color: var(--saffron-primary);
            padding: 6px 16px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .hero-title {{
            font-family: var(--font-heading);
            font-size: 2.35rem;
            font-weight: 800;
            line-height: 1.3;
            margin-bottom: 16px;
        }}
        .hero-title span {{
            background: linear-gradient(135deg, #f59e0b, #fbbf24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero-quote {{
            max-width: 960px;
            margin: 0 auto 24px auto;
            font-size: 1.05rem;
            color: var(--text-muted);
            line-height: 1.8;
            padding: 0 16px;
        }}

        /* Master 5-Hour Agenda Table */
        .agenda-table-card {{
            background: var(--bg-surface);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 24px;
            margin: 0 auto 28px auto;
            max-width: 1260px;
            box-shadow: var(--shadow-md);
            text-align: left;
        }}
        .agenda-table-header-wrap {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 10px;
        }}
        .agenda-table-title {{
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--saffron-primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .agenda-master-table-wrap {{
            width: 100%;
            overflow-x: auto;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
        }}
        .agenda-master-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            text-align: left;
        }}
        .agenda-master-table th {{
            background: var(--bg-card);
            color: var(--saffron-primary);
            font-family: var(--font-heading);
            font-weight: 800;
            padding: 14px 16px;
            border-bottom: 2px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            white-space: nowrap;
        }}
        .agenda-master-table td {{
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            vertical-align: top;
            background: var(--bg-surface);
            line-height: 1.65;
        }}
        .agenda-master-table tr:hover td {{
            background: var(--bg-card-hover);
        }}
        .agenda-master-table .col-title {{
            width: 25%;
            min-width: 200px;
        }}
        .agenda-master-table .col-brief {{
            width: 38%;
            min-width: 280px;
        }}
        .agenda-master-table .col-activities {{
            width: 37%;
            min-width: 280px;
        }}
        .session-badge-tag {{
            display: inline-block;
            background: rgba(245, 158, 11, 0.15);
            color: var(--saffron-primary);
            border: 1px solid var(--saffron-primary);
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 800;
            margin-bottom: 6px;
        }}
        .activity-bullet {{
            margin-bottom: 8px;
            padding-left: 18px;
            position: relative;
        }}
        .activity-bullet::before {{
            content: "•";
            position: absolute;
            left: 4px;
            color: var(--saffron-primary);
            font-weight: bold;
        }}

        /* Session Master Timer Bar */
        .timer-strip {{
            background: linear-gradient(90deg, rgba(245, 158, 11, 0.12), rgba(139, 92, 246, 0.12));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 14px 20px;
            margin: 0 auto 28px auto;
            max-width: 1260px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
        }}
        .timer-display {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-family: var(--font-heading);
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--saffron-primary);
        }}
        .timer-controls {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .btn-timer {{
            padding: 6px 14px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }}
        .btn-timer:hover {{
            border-color: var(--saffron-primary);
            color: var(--saffron-primary);
        }}
        .btn-timer-primary {{
            background: var(--saffron-primary);
            color: #000;
            border-color: var(--saffron-primary);
        }}
        .btn-timer-primary:hover {{
            background: #d97706;
            color: #000;
        }}

        /* Sticky Agenda Bar */
        .sticky-agenda-wrap {{
            position: sticky;
            top: 73px;
            z-index: 990;
            background: var(--bg-surface);
            border-bottom: 2px solid var(--saffron-primary);
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            padding: 10px 0;
            transition: all 0.3s;
        }}
        .agenda-cards-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }}
        .agenda-card-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            padding: 8px 12px;
            text-decoration: none;
            color: var(--text-main);
            display: flex;
            flex-direction: column;
            gap: 4px;
            transition: all 0.25s ease;
            position: relative;
            cursor: pointer;
        }}
        .agenda-card-btn:hover, .agenda-card-btn.active {{
            border-color: var(--saffron-primary);
            background: var(--bg-card-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 14px var(--saffron-glow);
        }}
        .agenda-card-btn.active {{
            border-left: 4px solid var(--saffron-primary);
        }}
        .agenda-card-btn .top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .agenda-card-btn .hour-tag {{
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--saffron-primary);
        }}
        .agenda-card-btn .dur-tag {{
            font-size: 0.7rem;
            color: var(--text-dim);
            font-weight: 700;
        }}
        .agenda-card-btn .topic-name {{
            font-family: var(--font-heading);
            font-size: 0.85rem;
            font-weight: 800;
            line-height: 1.25;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .agenda-card-btn .activity-peek {{
            font-size: 0.72rem;
            color: var(--text-muted);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* Section Block */
        .section-block {{
            padding: 56px 0 40px 0;
            border-bottom: 1px solid var(--border-color);
        }}
        .section-title-wrap {{
            margin-bottom: 32px;
        }}
        .section-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(245, 158, 11, 0.12);
            color: var(--saffron-primary);
            border: 1px solid rgba(245, 158, 11, 0.3);
            padding: 5px 14px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }}
        .section-heading {{
            font-family: var(--font-heading);
            font-size: 1.85rem;
            font-weight: 800;
            color: var(--text-main);
            line-height: 1.3;
            margin-bottom: 8px;
        }}
        .section-lead {{
            font-size: 1rem;
            color: var(--text-muted);
            max-width: 950px;
            line-height: 1.7;
        }}

        /* Card Grids */
        .card-grid-2 {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
            margin-top: 24px;
        }}
        .card-grid-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 24px;
        }}
        .card-grid-4 {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-top: 20px;
        }}

        /* Base Card */
        .base-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 24px;
            transition: all 0.25s ease;
        }}
        .base-card:hover {{
            border-color: rgba(245, 158, 11, 0.4);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }}

        /* Activity Card Accent */
        .activity-card-large {{
            background: var(--bg-surface);
            border: 2px solid rgba(245, 158, 11, 0.3);
            border-radius: var(--radius-lg);
            padding: 28px;
            margin: 24px 0;
            position: relative;
            box-shadow: var(--shadow-md);
        }}
        .activity-card-large::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 8px;
            height: 100%;
            background: linear-gradient(to bottom, #f59e0b, #d97706);
            border-top-left-radius: var(--radius-lg);
            border-bottom-left-radius: var(--radius-lg);
        }}
        .activity-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 16px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 14px;
        }}
        .activity-title {{
            font-family: var(--font-heading);
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .activity-meta {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .badge-pill {{
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 800;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }}

        /* Step List */
        .step-list {{
            list-style: none;
            margin: 16px 0;
        }}
        .step-list li {{
            position: relative;
            padding-left: 32px;
            margin-bottom: 12px;
            line-height: 1.65;
        }}
        .step-list li::before {{
            content: attr(data-step);
            position: absolute;
            left: 0;
            top: 2px;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            background: rgba(245, 158, 11, 0.15);
            color: var(--saffron-primary);
            border: 1px solid var(--saffron-primary);
            font-size: 0.75rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* Callouts */
        .quote-callout {{
            background: rgba(245, 158, 11, 0.08);
            border-left: 4px solid var(--saffron-primary);
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            padding: 16px 20px;
            margin: 16px 0;
            font-style: italic;
        }}
        .debrief-box {{
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: var(--radius-md);
            padding: 16px 20px;
            margin-top: 16px;
        }}
        .debrief-box strong {{
            color: #10b981;
        }}

        /* Interactive Widgets */
        .interactive-widget {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 24px;
            margin: 20px 0;
        }}

        /* 1-Minute Padmasana Timer */
        .meditation-timer-box {{
            text-align: center;
            padding: 30px;
            background: radial-gradient(circle at center, rgba(139, 92, 246, 0.15), transparent 70%);
            border: 2px dashed rgba(139, 92, 246, 0.4);
            border-radius: var(--radius-lg);
            margin: 20px 0;
        }}
        .meditation-countdown {{
            font-family: var(--font-heading);
            font-size: 4rem;
            font-weight: 900;
            color: #8b5cf6;
            margin: 10px 0;
            letter-spacing: 2px;
        }}

        /* Grain of Rice Chain Network */
        .rice-chain-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin: 16px 0;
        }}
        .rice-chain-node {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            padding: 12px;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .rice-chain-node:hover {{
            border-color: var(--saffron-primary);
        }}
        .rice-chain-node.broken {{
            border-color: #ef4444;
            background: rgba(239, 68, 68, 0.15);
            text-decoration: line-through;
            opacity: 0.6;
        }}

        /* Star Board Widget */
        .star-board-wrap {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 20px;
            margin: 20px 0;
        }}
        .star-columns-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 12px;
            margin: 16px 0;
        }}
        .star-col {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            padding: 14px 10px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .star-col-title {{
            font-weight: 800;
            font-size: 0.95rem;
            color: var(--saffron-primary);
        }}
        .star-count-display {{
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--text-main);
            min-height: 38px;
        }}
        .star-action-btns {{
            display: flex;
            justify-content: center;
            gap: 6px;
        }}
        .btn-star-pm {{
            width: 30px;
            height: 30px;
            border-radius: 50%;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            font-weight: 800;
            cursor: pointer;
            font-size: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .btn-star-pm:hover {{
            border-color: var(--saffron-primary);
            color: var(--saffron-primary);
        }}

        /* 200 Rishis Explorer */
        .rishi-toolbar {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }}
        .search-input-box {{
            flex: 1;
            min-width: 260px;
            position: relative;
        }}
        .search-input-box input {{
            width: 100%;
            padding: 12px 16px 12px 42px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            font-size: 0.95rem;
            outline: none;
            transition: border 0.2s;
        }}
        .search-input-box input:focus {{
            border-color: var(--saffron-primary);
        }}
        .search-input-box i {{
            position: absolute;
            left: 14px;
            top: 14px;
            color: var(--text-dim);
            width: 18px;
            height: 18px;
        }}
        .category-pill-group {{
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .btn-cat-pill {{
            padding: 7px 14px;
            border-radius: 999px;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
        }}
        .btn-cat-pill:hover, .btn-cat-pill.active {{
            background: var(--saffron-primary);
            color: #000;
            border-color: var(--saffron-primary);
        }}
        .rishi-list-scroll {{
            max-height: 520px;
            overflow-y: auto;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 12px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            background: var(--bg-surface);
        }}
        .rishi-item-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            padding: 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            transition: all 0.2s;
        }}
        .rishi-item-card:hover {{
            border-color: var(--saffron-primary);
            background: var(--bg-card-hover);
        }}
        .rishi-top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .rishi-num {{
            font-size: 0.72rem;
            font-weight: 800;
            color: var(--saffron-primary);
            background: rgba(245, 158, 11, 0.12);
            padding: 2px 8px;
            border-radius: 999px;
        }}
        .rishi-names {{
            font-family: var(--font-heading);
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--text-main);
        }}
        .rishi-names small {{
            font-size: 0.8rem;
            color: var(--text-dim);
            font-weight: 500;
            margin-left: 6px;
        }}
        .rishi-category-tag {{
            font-size: 0.75rem;
            color: #8b5cf6;
            font-weight: 700;
        }}
        .rishi-desc {{
            font-size: 0.84rem;
            color: var(--text-muted);
            line-height: 1.5;
        }}

        /* Balloon Arpanam Widget */
        .balloon-stage {{
            position: relative;
            min-height: 340px;
            background: radial-gradient(circle at center bottom, rgba(245, 158, 11, 0.15), rgba(7, 9, 14, 0.95));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-end;
            padding: 24px;
            margin: 20px 0;
        }}
        .floating-balloon {{
            width: 110px;
            height: 140px;
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            background: linear-gradient(135deg, #ef4444, #f59e0b);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-weight: 800;
            font-size: 0.85rem;
            text-align: center;
            padding: 8px;
            box-shadow: 0 10px 25px rgba(245, 158, 11, 0.4);
            position: relative;
            transition: all 1.8s cubic-bezier(0.25, 1, 0.5, 1);
            cursor: pointer;
        }}
        .floating-balloon::after {{
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-bottom: 10px solid #ef4444;
        }}
        .floating-balloon.released {{
            transform: translateY(-240px) scale(0.35);
            opacity: 0;
        }}
        .divine-light-glow {{
            position: absolute;
            top: 20px;
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(245, 158, 11, 0.5), transparent 70%);
            animation: pulseGlow 3s infinite alternate;
        }}
        @keyframes pulseGlow {{
            0% {{ transform: scale(0.9); opacity: 0.6; }}
            100% {{ transform: scale(1.2); opacity: 0.9; }}
        }}

        /* Footer */
        .page-footer {{
            background: var(--bg-surface);
            border-top: 1px solid var(--border-color);
            padding: 40px 0;
            text-align: center;
            color: var(--text-dim);
            font-size: 0.9rem;
        }}
        .page-footer a {{
            color: var(--saffron-primary);
            text-decoration: none;
            font-weight: 700;
        }}

        @media (max-width: 1024px) {{
            .agenda-cards-grid {{
                grid-template-columns: repeat(3, 1fr);
            }}
            .card-grid-3, .card-grid-4 {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .rice-chain-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .rishi-list-scroll {{
                grid-template-columns: 1fr;
            }}
        }}

        @media (max-width: 768px) {{
            .navbar-inner {{
                flex-direction: column;
                align-items: flex-start;
            }}
            .nav-actions {{
                width: 100%;
                justify-content: flex-end;
            }}
            .hero-title {{
                font-size: 1.75rem;
            }}
            .agenda-cards-grid {{
                grid-template-columns: 1fr;
            }}
            .card-grid-2, .card-grid-3, .card-grid-4 {{
                grid-template-columns: 1fr;
            }}
            .star-columns-grid {{
                grid-template-columns: 1fr;
            }}
            .rice-chain-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        /* ============================================================== */
        /* PRINT FORMAT STYLES — CONVERTED TO CLEAN TABLE WITHOUT SCROLLBARS */
        /* ============================================================== */
        @media print {{
            .navbar, .sticky-agenda-wrap, .btn-nav, .timer-strip, .btn-timer, .rishi-toolbar, 
            .category-pill-group, #ego-input, .search-input-box, #picked-rishis-display, 
            .star-action-btns, button, a.btn-timer {{
                display: none !important;
            }}
            body {{
                background: #ffffff !important;
                color: #000000 !important;
                font-size: 10pt !important;
                line-height: 1.45 !important;
            }}
            .container {{
                max-width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
                width: 100% !important;
            }}
            .hero {{
                padding: 10px 0 !important;
                background: none !important;
                border: none !important;
                text-align: left !important;
            }}
            .hero-badge-wrap {{
                display: none !important;
            }}
            .hero-title {{
                font-size: 1.6rem !important;
                color: #000 !important;
                margin-bottom: 6px !important;
                text-align: center !important;
            }}
            .hero-title span {{
                color: #000 !important;
                -webkit-text-fill-color: initial !important;
            }}
            .hero-quote {{
                font-size: 9pt !important;
                color: #222 !important;
                margin-bottom: 14px !important;
                padding: 0 !important;
                text-align: justify !important;
            }}
            
            /* Clean Full Table for Print */
            .agenda-table-card {{
                background: #ffffff !important;
                border: 2px solid #222 !important;
                padding: 10px !important;
                box-shadow: none !important;
                page-break-inside: avoid;
                margin: 10px 0 20px 0 !important;
                display: block !important;
                width: 100% !important;
            }}
            .agenda-table-title {{
                color: #000 !important;
                font-size: 12pt !important;
                font-weight: bold !important;
                margin-bottom: 8px !important;
            }}
            .agenda-master-table-wrap {{
                overflow: visible !important;
                border: 1px solid #333 !important;
                display: block !important;
                width: 100% !important;
            }}
            .agenda-master-table {{
                width: 100% !important;
                border-collapse: collapse !important;
                table-layout: fixed !important;
                display: table !important;
            }}
            .agenda-master-table th, .agenda-master-table td {{
                border: 1px solid #444 !important;
                background: #ffffff !important;
                color: #000000 !important;
                padding: 8px 10px !important;
                font-size: 8.5pt !important;
                word-wrap: break-word !important;
                overflow: visible !important;
                white-space: normal !important;
            }}
            .agenda-master-table th {{
                background: #f0f0f0 !important;
                font-weight: bold !important;
                color: #000 !important;
                border-bottom: 2px solid #000 !important;
            }}
            .session-badge-tag {{
                border: 1px solid #444 !important;
                color: #000 !important;
                background: #eee !important;
                padding: 2px 4px !important;
                font-size: 7.5pt !important;
            }}
            .row-title-text {{
                color: #000 !important;
                font-size: 9.5pt !important;
                font-weight: bold !important;
            }}
            .activity-bullet {{
                margin-bottom: 6px !important;
                font-size: 8.5pt !important;
                color: #111 !important;
            }}
            .activity-bullet::before {{
                color: #000 !important;
            }}
            .col-title {{
                width: 25% !important;
            }}
            .col-brief {{
                width: 38% !important;
            }}
            .col-activities {{
                width: 37% !important;
            }}

            /* All content cards print clean */
            .base-card, .activity-card-large, .interactive-widget {{
                border: 1px solid #777 !important;
                background: #ffffff !important;
                color: #000000 !important;
                page-break-inside: avoid;
                box-shadow: none !important;
                margin: 12px 0 !important;
                padding: 12px !important;
            }}
            .activity-card-large::before {{
                background: #444 !important;
                width: 4px !important;
            }}
            .quote-callout, .debrief-box {{
                background: #fafafa !important;
                border-color: #666 !important;
                color: #000 !important;
                page-break-inside: avoid;
            }}
            .rishi-list-scroll {{
                max-height: none !important;
                overflow: visible !important;
                display: block !important;
            }}
            .rishi-item-card {{
                break-inside: avoid;
                margin-bottom: 8px !important;
                border: 1px solid #ccc !important;
            }}
            * {{
                overflow: visible !important;
                box-shadow: none !important;
                text-shadow: none !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Navbar Header -->
    <header class="navbar">
        <div class="container">
            <div class="navbar-inner">
                <a href="#hero" class="brand">
                    <div class="brand-logo">
                        <i data-lucide="sun"></i>
                    </div>
                    <div class="brand-text">
                        <h1>அறம் — ஷட் கருமங்கள் பயிற்சிப் பட்டறை</h1>
                        <p>5 மணி நேர முழுமையான செயல்திட்டம் & நேரடிப் போதனை வழிகாட்டி</p>
                    </div>
                </a>

                <div class="nav-actions">
                    <a href="index.html" class="btn-nav" title="ஷட் கருமங்கள் முகப்பு பக்கம்">
                        <i data-lucide="home" style="width:16px; height:16px;"></i> முதன்மை முகப்பு
                    </a>
                    <button class="btn-nav" onclick="toggleTheme()" id="btn-theme" title="பின்னணி நிறத்தை மாற்றுக">
                        <i data-lucide="sun" id="theme-icon" style="width:16px; height:16px;"></i>
                        <span id="theme-label">Bright Theme</span>
                    </button>
                    <button class="btn-nav" onclick="window.print()" title="அச்சிட அல்லது PDF சேமிக்க">
                        <i data-lucide="printer" style="width:16px; height:16px;"></i> அச்சிடுக (Print)
                    </button>
                    <a href="#agenda-table-section" class="btn-nav btn-nav-primary">
                        <i data-lucide="table" style="width:16px; height:16px;"></i> அட்டவணை காண்க
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Banner -->
    <section class="hero" id="hero">
        <div class="container">
            <div class="hero-badge-wrap">
                <span class="hero-badge"><i data-lucide="flame" style="width:14px; height:14px;"></i> சனாதன தர்ம வாழ்வியல் தத்துவம்</span>
                <span class="hero-badge" style="border-color:#10b981; color:#10b981; background:rgba(16,185,129,0.12);"><i data-lucide="clock" style="width:14px; height:14px;"></i> 5 மணி நேர முழு செயல்திட்டம்</span>
                <span class="hero-badge" style="border-color:#8b5cf6; color:#8b5cf6; background:rgba(139,92,246,0.12);"><i data-lucide="sparkles" style="width:14px; height:14px;"></i> நேரடிப் போதனை &amp; செயல்பாடுகள்</span>
            </div>

            <h1 class="hero-title">
                கர்மா முதல் <span>நிஷ்காமியம்</span> வரை<br>
                5 மணி நேர முழுமையான பயிற்சிப் பட்டறை வழிகாட்டி
            </h1>

            <p class="hero-quote">
                <strong>“செயல் (கர்மா) என்பது உடலின் இயக்கம்; பந்தம் என்பது மனதின் ஆசை; யோகம் என்பது வாழ்வை பிரபஞ்சத்திற்கு அர்ப்பணிக்கும் கலை!”</strong><br>
                மனிதன் முதலில் கர்மாவின் இயல்பை உணர்ந்து, அதன் பந்தங்களிலிருந்து விடுபட்டு, பஞ்ச மகா யக்ஞங்கள் வழி கர்ம யோகியாக்கி, இறுதியில் தன்னலமற்ற நிஷ்காமிய நிலையை அடைவதற்கான 5 மணி நேரப் படிநிலைப் பயிற்சி வழிகாட்டி.
            </p>

            <!-- 5-Hour Master Agenda Table (Replaces scrollbar with clean printable table) -->
            <div class="agenda-table-card" id="agenda-table-section">
                <div class="agenda-table-header-wrap">
                    <div class="agenda-table-title">
                        <i data-lucide="calendar-check"></i>
                        <span>5 மணி நேர முழுமையான செயல்திட்ட அட்டவணை (5-Hour Master Workshop Curriculum Table)</span>
                    </div>
                    <span style="font-size:0.8rem; color:var(--text-muted); font-weight:700;">
                        அச்சிடும்போது முழுப் பக்க அட்டவணையாக விரியும் (Print-Friendly Format)
                    </span>
                </div>

                <div class="agenda-master-table-wrap">
                    <table class="agenda-master-table">
                        <thead>
                            <tr>
                                <th class="col-title"><i data-lucide="clock" style="width:14px; height:14px; display:inline;"></i> அமர்வு & தலைப்பு (Title & Duration)</th>
                                <th class="col-brief"><i data-lucide="book-open" style="width:14px; height:14px; display:inline;"></i> பாடச் சுருக்கம் (What is Covered)</th>
                                <th class="col-activities"><i data-lucide="play-circle" style="width:14px; height:14px; display:inline;"></i> நேரடிச் செயல்பாடுகள் & விவரங்கள் (Activity Names & Details)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Hour 1 -->
                            <tr>
                                <td class="col-title">
                                    <span class="session-badge-tag">மணி 1 • 60 நிமிடங்கள்</span>
                                    <h4 class="row-title-text" style="font-family:var(--font-heading); color:var(--saffron-primary); font-size:1.05rem; margin-bottom:4px;">
                                        1. கர்மா என்றால் என்ன? (What is Karma?)
                                    </h4>
                                    <small style="color:var(--text-dim); font-size:0.8rem;">நேரம்: 00:00 - 01:00</small><br>
                                    <a href="#hour-1" class="btn-timer" style="margin-top:8px; display:inline-flex; font-size:0.75rem; padding:3px 8px;">
                                        பகுதிக்குச் செல்க ➔
                                    </a>
                                </td>
                                <td class="col-brief">
                                    <ul style="margin:0; padding-left:16px;">
                                        <li><strong>செயல் தத்துவம்:</strong> கர்மா என்பது உடலாலும் உள்ளத்தாலும் செய்யும் செயல் (Action done by body and mind).</li>
                                        <li><strong>5 கர்மேந்திரியங்கள்:</strong> கை (செயல்), கால் (நடத்தல்), வாக்கு (பேச்சு), பாயு (கழிவுநீக்கம்), உபஸ்தம் (இனப்பெருக்கம்).</li>
                                        <li><strong>5 ஞானேந்திரியங்கள்:</strong> கண் (பார்வை), காது (கேட்டல்), மூக்கு (நுகர்தல்), நாக்கு (சுவை), தோல் (தொடுதல்).</li>
                                        <li><strong>மனதின் முக்கியத்துவம்:</strong> இந்திரியங்களுக்குப் பின்னால் மனம் இயங்கினால் மட்டுமே செயல் நடக்கும் (வகுப்பறை மாணவன், சினிமா தியேட்டர் உதாரணங்கள்).</li>
                                        <li><strong>சங்கல்பமே கர்மாவைத் தீர்மானிக்கிறது:</strong> மருத்துவர் மற்றும் திருடன் இருவரும் ஒரே கத்தியால் குத்தினாலும் மனதின் நோக்கமே புண்ணிய பாவத்தைத் தீர்மானிக்கிறது.</li>
                                    </ul>
                                </td>
                                <td class="col-activities">
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 1.1 — பந்து வீச்சு நீக்கல் விளையாட்டு:</strong> வட்டமாக அமர்ந்து பந்தை மாற்றி மாற்றி வீசுதல்; ஒரே நபருக்கு வீசினால் வெளியேற்றம். <em>பயன்பட்ட உறுப்பு: கை (கர்மேந்திரியம்).</em>
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 1.2 — காதில் ரகசிய வாக்கியத் தொடர் ஓட்டம்:</strong> <em>"ஒரு மனிதன் கோயிலுக்குள் செல்கிறான்; முதலில் தன்னையே அறிகிறான்..."</em> வாக்கியத்தை வரிசையாகக் காதில் ஓதி உருமாறுதலைக் கவனித்தல். <em>உறுப்பு: காது (ஞானேந்திரியம்).</em>
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 1.3 — இந்திரிய விரைவுப் பயிற்சி நிலைகள்:</strong> கண், மூக்கு (சந்தனம்/கற்பூரம்), நாக்கு (சுவை), தோல் (தொடுதல்) பரிசோதனைகள்.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 1.4 — 1-நிமிட பத்மாசன மௌன தியானம்:</strong> இந்திரியங்கள் அசைவற்று நின்றாலும் மனம் இடைவிடாது இயங்கிக் கொண்டே இருக்கிறது என்பதை உணரும் நேரடிப் பரிசோதனை.
                                    </div>
                                </td>
                            </tr>

                            <!-- Hour 2 -->
                            <tr>
                                <td class="col-title">
                                    <span class="session-badge-tag" style="border-color:#ef4444; color:#ef4444; background:rgba(239,68,68,0.12);">மணி 2 • 60 நிமிடங்கள்</span>
                                    <h4 class="row-title-text" style="font-family:var(--font-heading); color:#ef4444; font-size:1.05rem; margin-bottom:4px;">
                                        2. கர்ம பந்தம் என்றால் என்ன? (What is Karma Bandham?)
                                    </h4>
                                    <small style="color:var(--text-dim); font-size:0.8rem;">நேரம்: 01:00 - 02:00</small><br>
                                    <a href="#hour-2" class="btn-timer" style="margin-top:8px; display:inline-flex; font-size:0.75rem; padding:3px 8px;">
                                        பகுதிக்குச் செல்க ➔
                                    </a>
                                </td>
                                <td class="col-brief">
                                    <ul style="margin:0; padding-left:16px;">
                                        <li><strong>பந்தத்தின் தோற்றம்:</strong> கர்மாவில் குற்றமில்லை; அச்செயலோடு பந்தம் <strong>("நான்" Ahankara மற்றும் "எனது" Mamakara)</strong> இணையும் போதே துன்பம் உண்டாகிறது.</li>
                                        <li><strong>மூலக் காரணம்:</strong> காமம் (பேராசை, சுய நலம் மற்றும் கர்ம பலனைப் பிடித்துத் தொங்கும் எதிர்பார்ப்பு).</li>
                                        <li><strong>தனி மனித ஆற்றலின் பொய்மை:</strong> பிரபஞ்சத்தில் *"நான் தனியாக எதையுமே செய்துவிட முடியாது"* என்ற பிரபஞ்ச சார்புநிலை (Universal Interdependence).</li>
                                        <li><strong>குடும்ப பந்தம்:</strong> மனைவி, குழந்தைகள் மீது அன்பு செலுத்தும்போது பதிலுக்கு எதிர்பார்ப்புகளை வைப்பதால் மனக்கசப்பும் பந்தமும் உருவாகிறது; பலனை இறைவனிடம் விடும்போது அமைதி கிட்டுகிறது.</li>
                                    </ul>
                                </td>
                                <td class="col-activities">
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 2.1 — ஒரு பிடி சோற்றின் பிரபஞ்ச வலைப்பின்னல்:</strong> தட்டில் உள்ள ஒரு கவளம் சோறு நம்மை அடைய மண், சூரியன், மழை, மண்புழு, உழவு மாடு, உழவர், லாரி டிரைவர், மண்டி, மளிகைக் கடை, உப்பு, பாத்திரம், சிலிண்டர் என 16 அமைப்புகள் தேவைப்படுவதைக் கண்டறிதல்.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 2.2 — சங்கிலி முறிவு பரிசோதனை:</strong> ஏதேனும் ஓர் இணைப்பு இல்லாவிட்டாலும் உணவு கிடைக்காது என உணர்ந்து, 'நான் சம்பாதித்தேன்' என்ற அகந்தையைக் களையும் நேரடி ஆய்வு.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 2.3 — எதிர்பார்ப்பு vs விடுதலை தராசு:</strong> கடமையை 100% நேர்த்தியாகச் செய்துவிட்டு அதன் பலனை இறைவன்/காலத்தின் கைகளில் விட்டுவிடும் விவேகப் பயிற்சி.
                                    </div>
                                </td>
                            </tr>

                            <!-- Hour 3 -->
                            <tr>
                                <td class="col-title">
                                    <span class="session-badge-tag" style="border-color:#10b981; color:#10b981; background:rgba(16,185,129,0.12);">மணி 3 • 60 நிமிடங்கள்</span>
                                    <h4 class="row-title-text" style="font-family:var(--font-heading); color:#10b981; font-size:1.05rem; margin-bottom:4px;">
                                        3. ஷட் கருமங்களின் விரிவான விளக்கம் (Detailing of Karma)
                                    </h4>
                                    <small style="color:var(--text-dim); font-size:0.8rem;">நேரம்: 02:00 - 03:00</small><br>
                                    <a href="#hour-3" class="btn-timer" style="margin-top:8px; display:inline-flex; font-size:0.75rem; padding:3px 8px;">
                                        பகுதிக்குச் செல்க ➔
                                    </a>
                                </td>
                                <td class="col-brief">
                                    <ul style="margin:0; padding-left:16px;">
                                        <li><strong>நித்ய கர்மா (Nitya):</strong> தினசரி செய்ய வேண்டிய கட்டாயக் கடமைகள் (விழிப்பு, தூய்மை, சூரிய நமஸ்காரம், சந்தியாவந்தனம், பஞ்ச யக்ஞம்).</li>
                                        <li><strong>நைமித்திக கர்மா (Naimittika):</strong> அமாவாசை தர்ப்பணம், திதி, பண்டிகைகள், 16 சம்ஸ்கார காலக் கடமைகள்.</li>
                                        <li><strong>காம்ய கர்மா (Kamya):</strong> சுய ஆசை மற்றும் பலாபலன்களை முன்னிறுத்திச் செய்யப்படும் விருப்பக் கர்மாக்கள்.</li>
                                        <li><strong>நிஷ்காம்ய கர்மா (Nishkamya):</strong> பலன் எதிர்பாராது லோக க்ஷேமத்திற்காகவும் இறை அர்ப்பணமாகவும் செய்யப்படும் தூய சேவை.</li>
                                        <li><strong>பிராயச்சித்த கர்மா (Prayaschitta):</strong> செய்த தவறுகளுக்கு வருந்தி மனச்சுத்தி தேடும் பரிகாரங்கள் (விரதம், தானம், மரம் நடுதல்).</li>
                                        <li><strong>நிஷித்த கர்மா (Nishiddha):</strong> அறத்திற்குப் புறம்பான, அறவே தவிர்க்கப்பட வேண்டிய 44 தீய பாவச் செயல்கள்.</li>
                                    </ul>
                                </td>
                                <td class="col-activities">
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 3.1 — 12 நிஜ வாழ்க்கைச் சூழல் வகைப்பாட்டு போட்டி:</strong> அமாவாசை தர்ப்பணம், விபத்து முதலுதவி, லஞ்சம் கொடுத்தல், பரீட்சை அர்ச்சனை... போன்ற 12 சூழல்களுக்கான கர்ம வகையை அடையாளம் காணும் ஊடாடும் வினாடி வினா.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 3.2 — காம்யத்திலிருந்து நிஷ்காமியத்திற்கு மாற்றும் பயிற்சி:</strong> சுய நலத்திற்காகச் செய்யும் சமையல், உழைப்பு, கல்வியை பிறர் பசி தீர்க்கும் மற்றும் இறை அர்ப்பண சேவையாக மாற்றும் மனோபாவப் பயிற்சி.
                                    </div>
                                </td>
                            </tr>

                            <!-- Hour 4 -->
                            <tr>
                                <td class="col-title">
                                    <span class="session-badge-tag" style="border-color:#3b82f6; color:#3b82f6; background:rgba(59,130,246,0.12);">மணி 4 • 75 நிமிடங்கள்</span>
                                    <h4 class="row-title-text" style="font-family:var(--font-heading); color:#3b82f6; font-size:1.05rem; margin-bottom:4px;">
                                        4. பஞ்ச மகா யக்ஞம் வழி கர்ம யோகம் (Karma as Karma Yoga)
                                    </h4>
                                    <small style="color:var(--text-dim); font-size:0.8rem;">நேரம்: 03:00 - 04:15</small><br>
                                    <a href="#hour-4" class="btn-timer" style="margin-top:8px; display:inline-flex; font-size:0.75rem; padding:3px 8px;">
                                        பகுதிக்குச் செல்க ➔
                                    </a>
                                </td>
                                <td class="col-brief">
                                    <ul style="margin:0; padding-left:16px;">
                                        <li><strong>பித்ரு யக்ஞம்:</strong> பெற்றோர் வழிபாடு; மனிதன் வெறும் Hardware ஆகப் பிறக்கிறான் (Software ஏற்றுவது பெற்றோரே). முதுமையில் அவர்கள் குழந்தையாவதால் காப்பது கடமை.</li>
                                        <li><strong>பூத யக்ஞம்:</strong> இயற்கையின் 10 கொடைகள்; ஆவுரஞ்சிக் கல், மரம் நடுதல்; பூமி 10 மில்லியன் வகை உயிர்களுக்கும் சொந்தமானது.</li>
                                        <li><strong>நர / மனுஷ்ய யக்ஞம்:</strong> சமுதாயத் தொழிலாளர்களுக்கு நன்றி, கருணை, நியாயமான ஊதியம், அதிதி உபசரிப்பு.</li>
                                        <li><strong>ரிஷி யக்ஞம்:</strong> நைமிசாரண்யத்தில் 100 ஆண்டுக்கொருமுறை கூடிய மகா சபை; பண்டிகைகள் & 16 சம்ஸ்காரங்கள் வகுத்த ரிஷிகள்; ரிஷி நூல் படித்து வாழ்வாக்குதல்.</li>
                                        <li><strong>தெய்வ யக்ஞம்:</strong> மாணிக்கவாசகர் சிவபுராண பாராயணம்; உடலின் 4 தானியங்கி அற்புதங்கள் (இதயம், செரிமானம்...); பிரபஞ்ச ஜூம் & <strong>தத்துவமசி</strong>.</li>
                                    </ul>
                                </td>
                                <td class="col-activities">
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 4.1 — நட்சத்திர நினைவுக் கட்டப் பலகை (0-5 vs >60 வயது):</strong> 10 நட்சத்திரங்களைப் பகிர்ந்து வைத்து, குழந்தைப் பருவத்திலும் முதுமையிலும் பெற்றோர் நம்மைக் காப்பதையும் நாம் அவர்களைக் காப்பதையும் உணர்தல்.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 4.2 — பூத யக்ஞ 10 கொடைகள் ஆய்வு:</strong> மரங்கள் (O2), தேனீக்கள் (மகரந்தம்), மண்புழுக்களின் நன்மையை உணர்ந்து நீர் & நிலம் காக்கும் உறுதிமொழி.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 4.3 — நர யக்ஞ இரு அணிகள் விவாதச் சங்கிலி:</strong> ஆசிரியர், துப்புரவுப் பணியாளர், உழவர்... என சமுதாயத் தொழிலாளர்களின் பணிகளை மாறி மாறிக் கூறி நன்றி பாராட்டுதல்.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 4.4 — பாரதத்தின் 200 ரிஷிகள் தேடல் & 2 ரிஷிகள் தேர்வு:</strong> 200 ரிஷிகள் பட்டியலை ஆராய்ந்து தன் வாழ்விற்கான 2 வழிகாட்டி ரிஷிகளைத் தேர்ந்தெடுத்தல்.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 4.5 — சிவபுராண கூட்டுப் பாராயணம் & பிரபஞ்ச ஜூம்:</strong> அரங்கம் முதல் 2 லட்சம் கோடி விண்மீன் மண்டலங்கள் வரை அளவிட்டு அகந்தையைக் கரைத்தல்.
                                    </div>
                                </td>
                            </tr>

                            <!-- Hour 5 -->
                            <tr>
                                <td class="col-title">
                                    <span class="session-badge-tag" style="border-color:#8b5cf6; color:#8b5cf6; background:rgba(139,92,246,0.12);">மணி 5 • 45 நிமிடங்கள்</span>
                                    <h4 class="row-title-text" style="font-family:var(--font-heading); color:#8b5cf6; font-size:1.05rem; margin-bottom:4px;">
                                        5. சுயநலமற்ற நிஷ்காமியப் பயிற்சி & சங்கல்பம் (Slowly Practice Nishkamya)
                                    </h4>
                                    <small style="color:var(--text-dim); font-size:0.8rem;">நேரம்: 04:15 - 05:00</small><br>
                                    <a href="#hour-5" class="btn-timer" style="margin-top:8px; display:inline-flex; font-size:0.75rem; padding:3px 8px;">
                                        பகுதிக்குச் செல்க ➔
                                    </a>
                                </td>
                                <td class="col-brief">
                                    <ul style="margin:0; padding-left:16px;">
                                        <li><strong>4 ஆசிரம நிலைகள்:</strong> பிரம்மச்சர்யம் (கல்வி) ➔ கிரஹஸ்தம் (குடும்பம்/தியாகம்) ➔ வானபிரஸ்தம் (பொதுப்பணி) ➔ சன்யாசம் (பேரன்பு/முக்தி).</li>
                                        <li><strong>குடும்பமே ஆன்மீக உலைக்களம்:</strong> மனைவி, குழந்தைகள், பெற்றோருக்காகத் தன் தூக்கத்தையும் உணவையும் தியாகம் செய்து *நான் ➔ குடும்பம் ➔ சமுதாயம் ➔ தேசம் ➔ பிரபஞ்சம்* என அன்பை விரித்தல்.</li>
                                        <li><strong>கைகளை விடுவித்தல்:</strong> பற்றுகளைப் பிடித்துத் தொங்குவதை விடுத்து இறைவனிடம் சமர்ப்பித்தால் மட்டுமே இரு கைகளாலும் பிறருக்குச் சேவை செய்ய முடியும்.</li>
                                        <li><strong>நிறைவு சங்கல்பம்:</strong> வாழ்நாள் முழுவதும் கடைப்பிடிக்க வேண்டிய 5 நன்னெறி உறுதிமொழிகள்.</li>
                                    </ul>
                                </td>
                                <td class="col-activities">
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 5.1 — ஈஸ்வர சமர்ப்பண பலூன் / காகிதப் பற்று நீக்கும் பயிற்சி:</strong> தன் அகந்தை, கோபம், பாராட்டு ஆசையை எழுதி சமர்ப்பிக்கையில் பலூன் ஒளிப்பிழம்பில் கரைந்து கைகள் விடுபடும் சிமுலேட்டர்.
                                    </div>
                                    <div class="activity-bullet">
                                        <strong>செயல்பாடு 5.2 — 5-அம்ச வாழ்நாள் நிறைவுச் சங்கல்பம்:</strong> நித்ய விழிப்பு, பெற்றோர் வழிபாடு, இயற்கைப் பாதுகாப்பு, நிஷ்காமியச் சேவை மற்றும் பணிவுக்கான உறுதிமொழி ஏற்பு.
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Master Session Timer Widget -->
            <div class="timer-strip">
                <div class="timer-display">
                    <i data-lucide="timer" style="width:24px; height:24px;"></i>
                    <span id="session-clock">05:00:00</span>
                    <span style="font-size:0.8rem; color:var(--text-muted); font-weight:600;">(அமர்வு நேரக் கடிகாரம்)</span>
                </div>
                <div class="timer-controls">
                    <button class="btn-timer btn-timer-primary" onclick="toggleSessionTimer()" id="btn-session-timer">
                        <i data-lucide="play" style="width:14px; height:14px;" id="timer-btn-icon"></i>
                        <span id="timer-btn-text">டைமர் தொடங்கு</span>
                    </button>
                    <button class="btn-timer" onclick="resetSessionTimer()">
                        <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i> மீட்டமை
                    </button>
                    <button class="btn-timer" onclick="playTempleBellSound()" title="ஆலய மணி ஒலி சோதிக்க">
                        <i data-lucide="bell" style="width:14px; height:14px;"></i> மணி ஒலி
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- Top Agenda Interactive Navigator -->
    <div class="sticky-agenda-wrap">
        <div class="container">
            <div class="agenda-cards-grid">
                <!-- Hour 1 -->
                <a href="#hour-1" class="agenda-card-btn active" id="agenda-link-1">
                    <div class="top-row">
                        <span class="hour-tag">மணி 1 (Hour 1)</span>
                        <span class="dur-tag">60 நிமி</span>
                    </div>
                    <div class="topic-name">1. கர்மா என்றால் என்ன?</div>
                    <div class="activity-peek">⚽ பந்து வீச்சு • 👂 ரகசிய வாக்கியம் • 🧘 மௌன தியானம்</div>
                </a>

                <!-- Hour 2 -->
                <a href="#hour-2" class="agenda-card-btn" id="agenda-link-2">
                    <div class="top-row">
                        <span class="hour-tag">மணி 2 (Hour 2)</span>
                        <span class="dur-tag">60 நிமி</span>
                    </div>
                    <div class="topic-name">2. கர்ம பந்தம் (நான் & எனது)</div>
                    <div class="activity-peek">🌾 ஒரு பிடி சோற்றின் வலைப்பின்னல் • ⚖️ எதிர்பார்ப்பு தராசு</div>
                </a>

                <!-- Hour 3 -->
                <a href="#hour-3" class="agenda-card-btn" id="agenda-link-3">
                    <div class="top-row">
                        <span class="hour-tag">மணி 3 (Hour 3)</span>
                        <span class="dur-tag">60 நிமி</span>
                    </div>
                    <div class="topic-name">3. ஷட் கருமங்களின் விளக்கம்</div>
                    <div class="activity-peek">📊 12 சூழல் வகைப்பாட்டு பலகை • 🔄 காம்ய ➔ நிஷ்காமிய மாற்றம்</div>
                </a>

                <!-- Hour 4 -->
                <a href="#hour-4" class="agenda-card-btn" id="agenda-link-4">
                    <div class="top-row">
                        <span class="hour-tag">மணி 4 (Hour 4)</span>
                        <span class="dur-tag">75 நிமி</span>
                    </div>
                    <div class="topic-name">4. பஞ்ச மகா யக்ஞம் வழி யோகம்</div>
                    <div class="activity-peek">⭐ நட்சத்திர பலகை • 📜 200 ரிஷிகள் • 🌌 பிரபஞ்ச ஜூம்</div>
                </a>

                <!-- Hour 5 -->
                <a href="#hour-5" class="agenda-card-btn" id="agenda-link-5">
                    <div class="top-row">
                        <span class="hour-tag">மணி 5 (Hour 5)</span>
                        <span class="dur-tag">45 நிமி</span>
                    </div>
                    <div class="topic-name">5. நிஷ்காமியப் பயிற்சி & சங்கல்பம்</div>
                    <div class="activity-peek">🎈 பற்று நீக்கும் பலூன் • 🏡 4 ஆசிரமங்கள் • 📜 நிறைவு உறுதிமொழி</div>
                </a>
            </div>
        </div>
    </div>

    <main class="main-layout">
        <div class="container">

            <!-- ========================================== -->
            <!-- TOPIC 1: WHAT IS KARMA? (HOUR 1) -->
            <!-- ========================================== -->
            <section class="section-block" id="hour-1">
                <div class="section-title-wrap">
                    <span class="section-badge"><i data-lucide="activity"></i> மணி 1 • முதல் அமர்வு (00:00 - 01:00)</span>
                    <h2 class="section-heading">1. கர்மா என்றால் என்ன? (What is Karma?) — உடலின் செயல், புலன்கள் &amp; மனதின் சக்தி</h2>
                    <p class="section-lead">
                        கர்மா என்றால் வெறுமனே விதி அல்லது முற்பிறவிப் பலன் மட்டுமல்ல; மிக அடிப்படையாக <strong>“நாம் உடலாலும் உள்ளத்தாலும் செய்யும் செயல்”</strong> (Action done using our body and mind).
                        நமது ஸ்தூல உடல் 5 கர்மேந்திரியங்கள் மற்றும் 5 ஞானேந்திரியங்கள் வழியே இந்த உலகத்தோடு தொடர்பு கொண்டு செயல்களைப் புரிகிறது.
                    </p>
                </div>

                <!-- 5 Karmendriyas & 5 Gnanendriyas Cards -->
                <div class="card-grid-2">
                    <div class="base-card" style="border-top: 4px solid var(--saffron-primary);">
                        <h3 style="font-family:var(--font-heading); color:var(--saffron-primary); margin-bottom:12px; display:flex; align-items:center; gap:8px;">
                            <i data-lucide="hand"></i> 5 கர்மேந்திரியங்கள் (Organs of Action)
                        </h3>
                        <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:14px;">
                            புறவுலகில் நேரடியாகச் செயல்களை நிகழ்த்தும் உடலின் ஐந்து செயலாற்றல் உறுப்புகள்:
                        </p>
                        <ul class="step-list">
                            <li data-step="1"><strong>கை (பாணி / Hasta):</strong> பொருட்களை எடுத்தல், கொடுத்தல், எழுதுதல், தொண்டு செய்தல்.</li>
                            <li data-step="2"><strong>கால் (பாதம் / Pada):</strong> நடத்தல், பயணம் செய்தல், தர்ம வழி செல்லுதல்.</li>
                            <li data-step="3"><strong>வாய் / வாக்கு (வாக் / Vaak):</strong> பேசுதல், பாடுதல், மந்திர உச்சரிப்பு, சுவை உணர்தல்.</li>
                            <li data-step="4"><strong>பாயு (எருவாய் / Payu):</strong> மலக்கழிவு மற்றும் நச்சுக்களை வெளியேற்றுதல் (தூய்மை).</li>
                            <li data-step="5"><strong>உபஸ்தம் (கருவாய் / Upastha):</strong> இனப்பெருக்கம், ஜீவ உற்பத்தி மற்றும் சிற்றின்பம்.</li>
                        </ul>
                    </div>

                    <div class="base-card" style="border-top: 4px solid #3b82f6;">
                        <h3 style="font-family:var(--font-heading); color:#3b82f6; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
                            <i data-lucide="eye"></i> 5 ஞானேந்திரியங்கள் (Organs of Perception)
                        </h3>
                        <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:14px;">
                            பிரபஞ்சத்தின் ஐந்து தன்மாத்திரைகளை (ரூப, சப்த, கந்த, ரச, ஸ்பர்ச) மூளைக்குக் கொண்டு சேர்க்கும் ஐம்புலன்கள்:
                        </p>
                        <ul class="step-list">
                            <li data-step="1"><strong>கண் (சக்ஷு / Netra):</strong> உருவம், நிறம் மற்றும் அழகைப் பார்த்தல் (ரூபம்).</li>
                            <li data-step="2"><strong>காது (சுரோத்திரம் / Karna):</strong> ஓசை, சொற்கள் மற்றும் நாதத்தைக் கேட்டல் (சப்தம்).</li>
                            <li data-step="3"><strong>மூக்கு (கிராணம் / Nasika):</strong> நறுமணம் மற்றும் நாற்றத்தை நுகர்தல் (கந்தம்).</li>
                            <li data-step="4"><strong>நாக்கு (ஜிஹ்வா / Jihva):</strong> அறுசுவைகளை அறிதல் மற்றும் உணர்தல் (ரஸம்).</li>
                            <li data-step="5"><strong>தோல் (த்வக் / Sparsha):</strong> குளிர், வெப்பம், மென்மை, வலியை உணர்தல் (ஸ்பரிசம்).</li>
                        </ul>
                    </div>
                </div>

                <!-- ACTIVITY 1.1: BALL PASSING ELIMINATION GAME -->
                <div class="activity-card-large">
                    <div class="activity-header">
                        <div class="activity-title">
                            <i data-lucide="play-circle" style="color:var(--saffron-primary);"></i>
                            செயல்பாடு 1.1: பந்து வீச்சு நீக்கல் விளையாட்டு (Ball Passing Elimination Game)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="clock"></i> 10 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(16,185,129,0.15); color:#10b981;"><i data-lucide="hand"></i> கை (கர்மேந்திரியம்)</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>நோக்கம்:</strong> கர்மாவை உடலின் உறுப்புகள் எவ்வாறு இயற்றுகின்றன என்பதையும், விழிப்புணர்வின்றி செய்யும் செயல் எவ்வாறு பிழையை (பாவம்/தோல்வி) உருவாக்குகிறது என்பதையும் நேரடியாக உணர்தல்.
                    </p>

                    <ul class="step-list">
                        <li data-step="1">பயிற்சியில் கலந்துகொள்வோரை 8 முதல் 10 பேர் கொண்ட வட்டங்களாக அமர அல்லது நிற்க வைக்கவும்.</li>
                        <li data-step="2">ஒரு மென்மையான பந்தைக் கொடுத்து, ஒருவருக்கொருவர் மாற்றி மாற்றி வேகமாக வீச வேண்டும்.</li>
                        <li data-step="3"><strong>முக்கிய விதி:</strong> பந்தை தனக்கு வீசிய அதே நபருக்கோ அல்லது உடனே தன் அருகிலுள்ளவருக்கோ வீசக்கூடாது; ஒரே நபருக்கு மீண்டும் மீண்டும் வீசினால் அந்த அணி ஆட்டத்திலிருந்து நீக்கப்படும் (Eliminated).</li>
                        <li data-step="4">பந்து கீழே விழுந்தாலும் அல்லது தவறான நபருக்கு வீசினாலும் குறிப்பிட்ட நபர்/அணி வெளியேறும். இறுதி வரை பிழையின்றி விளையாடும் அணி வெற்றி பெறும்.</li>
                    </ul>

                    <div class="debrief-box">
                        <strong>🎯 ஆய்வுக் கேள்வி & போதனை (Debrief Question):</strong><br>
                        <em>“இந்தப் பந்து வீச்சு கர்மாவைச் செய்ய உங்கள் உடலில் எந்த இந்திரியம் மிக முக்கியமாகப் பயன்பட்டது?”</em><br>
                        👉 விடை: <strong>கை (கர்மேந்திரியம் / Hand)</strong>. ஒரு கர்மாவைச் செய்ய உடலின் உறுப்பு இன்றியமையாதது என்பதை அனைவரும் புரிந்து கொள்கின்றனர்.
                    </div>
                </div>

                <!-- ACTIVITY 1.2: WHISPER RELAY SENTENCE -->
                <div class="activity-card-large">
                    <div class="activity-header">
                        <div class="activity-title">
                            <i data-lucide="volume-2" style="color:#3b82f6;"></i>
                            செயல்பாடு 1.2: காதில் ரகசிய வாக்கியத் தொடர் ஓட்டம் (Whisper Relay Sentence)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(59,130,246,0.15); color:#3b82f6;"><i data-lucide="clock"></i> 10 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(139,92,246,0.15); color:#8b5cf6;"><i data-lucide="ear"></i> காது (ஞானேந்திரியம்)</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>நோக்கம்:</strong> ஞானேந்திரியமான காது ஒலியை எவ்வாறு உள்வாங்குகிறது, புலனின் கவனக்குறைவால் உண்மை எவ்வாறு திரிபடைந்து கர்மப் பிழையாக மாறுகிறது என்பதை அறிதல்.
                    </p>

                    <div class="quote-callout" style="border-left-color:#3b82f6;">
                        <strong>காகிதத்தில் எழுதப்பட வேண்டிய புனித வாக்கியம்:</strong><br>
                        <em>“ஒரு மனிதன் கோயிலுக்குள் செல்கிறான்; முதலில் தன்னையே அறிகிறான், பின் மெல்ல மெல்ல இறைவனோடு இரண்டறக் கலக்கிறான்.”</em><br>
                        <small style="color:var(--text-dim);">(A person enters the temple; first discovers himself, then slowly merges into the Divine.)</small>
                    </div>

                    <ul class="step-list">
                        <li data-step="1">முதல் நபரிடம் மட்டும் இந்தக் குறிப்புத் தாள் இரகசியமாகக் காண்பிக்கப்படுகிறது.</li>
                        <li data-step="2">அவர் அடுத்தவரின் காதில் ஒரே ஒரு முறை மட்டுமே இரகசியமாக மெல்லிய குரலில் ஓத வேண்டும்.</li>
                        <li data-step="3">இவ்வாறாக வரிசையில் உள்ள 8-10 பேரின் காதுகளிலும் ஒருவர் பின் ஒருவராகச் சொல்லப்பட்டு, இறுதி நபரை வந்தடைகிறது.</li>
                        <li data-step="4">இறுதி நபர் தான் கேட்டதை மேடையில் சத்தமாக உரைப்பார். அதன் பின் அசல் தாள் உரக்க வாசிக்கப்படும். வார்த்தைகள் முற்றிலுமாக உருமாறியிருக்கும் நகைச்சுவை மற்றும் ஆச்சரியம் வெளிப்படும்!</li>
                    </ul>

                    <div class="debrief-box" style="border-color:#3b82f6; background:rgba(59,130,246,0.08);">
                        <strong style="color:#3b82f6;">🎯 ஆய்வுக் கேள்வி & போதனை:</strong><br>
                        <em>“இந்தச் செயலில் பிரதானமாக இயங்கிய உறுப்பு எது?”</em><br>
                        👉 விடை: <strong>காது (ஞானேந்திரியம் / Ear)</strong>. புலன்கள் சரியாக விழிப்போடு இல்லாவிட்டால் தகவல் மாறுபட்டு விபரீதமான கர்ம விளைவுகளை உருவாக்கும்.
                    </div>
                </div>

                <!-- SENSORY STATIONS (EYE, NOSE, TASTE, SKIN, LEGS) -->
                <div class="interactive-widget">
                    <h3 style="font-family:var(--font-heading); color:var(--saffron-primary); margin-bottom:10px;">
                        <i data-lucide="sparkles"></i> பிற இந்திரியங்களுக்கான விரைவுப் பயிற்சி நிலைகள் (Quick Sensory Stations)
                    </h3>
                    <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:16px;">
                        நேரக் கணக்கீட்டின்படி (Time Check), பின்வரும் உறுப்புகளையும் விரைவாகச் சோதிக்கலாம்:
                    </p>
                    <div class="card-grid-3">
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:6px;"><i data-lucide="eye"></i> கண் (பார்வைக் கர்மா)</h4>
                            <p style="font-size:0.84rem; color:var(--text-muted);">
                                10 புனிதப் பொருட்களைத் தட்டில் 10 நொடிகள் காட்டி மூடிவிடவும். பார்த்த பொருட்களை நினைவுகூர்ந்து எழுதச் சொல்லுதல் (த்ருஷ்டி கர்மா).
                            </p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#f59e0b; margin-bottom:6px;"><i data-lucide="wind"></i> மூக்கு (நறுமணக் கர்மா)</h4>
                            <p style="font-size:0.84rem; color:var(--text-muted);">
                                கண்களை மூடிக்கொண்டு கற்பூரம், சந்தனம், மல்லிகை, வேப்பிலை நறுமணத்தை நுகர்ந்து சரியாகக் கண்டறியும் கந்த பரிசோதனை.
                            </p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#8b5cf6; margin-bottom:6px;"><i data-lucide="smile"></i> நாக்கு &amp; கால் (சுவை &amp; நடை)</h4>
                            <p style="font-size:0.84rem; color:var(--text-muted);">
                                பிரசாதத்தை அவசரமின்றி நாவில் வைத்து சுவையை உணர்தல்; தாள லயத்தோடு கால்களை எடுத்து வைக்கும் பாத கர்மா.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- CRITICAL PIVOT: IS THAT ALL KARMA? -->
                <div class="quote-callout" style="border-left-color:#ef4444; background:rgba(239,68,68,0.08); margin:28px 0;">
                    <h3 style="color:#ef4444; font-family:var(--font-heading); font-size:1.3rem; margin-bottom:6px;">
                        ❓ ஆழமான கேள்வி: உடலால் செய்யும் செயல் மட்டுமே கர்மாவா? (Is that all Karma?)
                    </h3>
                    <p style="font-size:1rem; color:var(--text-main);">
                        கை, கால், கண், காதுகளை வைத்துச் செய்யும் செயல்களோடு கர்மா முடிந்துவிட்டதா? உடலின் அனைத்து இந்திரியங்களையும் முற்றிலுமாக நிறுத்திவிட்டால் கர்மாவும் நின்றுவிடுமா? இதோ அடுத்த நேரடிப் பரிசோதனை!
                    </p>
                </div>

                <!-- ACTIVITY 1.3: 1-MINUTE PADMASANA SILENCE & MIND REVELATION -->
                <div class="activity-card-large" style="border-color:#8b5cf6;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:#8b5cf6;">
                            <i data-lucide="brain"></i>
                            செயல்பாடு 1.3: 1-நிமிட பத்மாசன முழு அமைதி &amp; மனதின் விழிப்புணர்வுப் பரிசோதனை
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(139,92,246,0.15); color:#8b5cf6;"><i data-lucide="clock"></i> 60 நொடிகள் தியானம்</span>
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="zap"></i> மனம் (அந்தக்கரணம்)</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>பயிற்றுநர் வழிகாட்டல்:</strong> அரங்கில் உள்ள அனைவரும் பத்மாசனம் அல்லது சுகாசனத்தில் அமர்ந்து, கைகளைக் கூப்பி, கண்களை மூடி, மூச்சடக்கி ஊசி விழும் பேரமைதியில் (Pin-drop silence) 1 நிமிடம் இருக்க வேண்டும்.
                    </p>

                    <!-- Interactive 1-Minute Meditation Timer Widget -->
                    <div class="meditation-timer-box">
                        <p style="font-size:0.95rem; font-weight:700; color:var(--text-muted);">🧘 1 நிமிட பத்மாசன மௌன தியான டைமர்</p>
                        <div class="meditation-countdown" id="meditation-timer-display">01:00</div>
                        <div style="display:flex; justify-content:center; gap:10px;">
                            <button class="btn-timer btn-timer-primary" onclick="startMeditationTimer()" id="btn-med-timer">
                                <i data-lucide="play" style="width:14px; height:14px;"></i> தியானம் தொடங்கு
                            </button>
                            <button class="btn-timer" onclick="resetMeditationTimer()">
                                <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i> மீட்டமை
                            </button>
                        </div>
                    </div>

                    <div class="debrief-box" style="border-color:#8b5cf6; background:rgba(139,92,246,0.08);">
                        <strong style="color:#8b5cf6; font-size:1.1rem;">🎯 1 நிமிடத்திற்குப் பின் பயிற்றுநர் கேட்கும் கேள்வி:</strong><br>
                        <em>“இப்போது உங்கள் 5 கர்மேந்திரியங்களும் 5 ஞானேந்திரியங்களும் அசைவின்றி நிறுத்தப்பட்டுவிட்டன. ஆனாலும் உங்களுக்குள் கர்மா (செயல்) நடந்ததாக உணர்கிறீர்களா?”</em><br><br>
                        அரங்கில் உள்ளோர்: <strong>“ஆம்!” (Yes!)</strong><br>
                        👉 <strong>மகா உண்மை:</strong> உடல் இந்திரியங்கள் அனைத்தும் அசைவற்று நின்றாலும், <strong>மனம் (MIND)</strong> தொடர்ந்து இயங்கிக்கொண்டே இருக்கிறது! எண்ணங்களும் சங்கல்பங்களும் மனக்கண்ணில் பல்லாயிரக்கணக்கில் ஓடிக்கொண்டிருக்கின்றன.
                    </div>

                    <!-- Examples of Mind Dominance -->
                    <div class="card-grid-2" style="margin-top:20px;">
                        <div class="base-card">
                            <h4 style="color:var(--saffron-primary); margin-bottom:8px;"><i data-lucide="graduation-cap"></i> உதாரணம் 1: வகுப்பறையில் மாணவன்</h4>
                            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                                மாணவன் உடலால் நேராக அமர்ந்து ஆசிரியரை தன் கண்களால் பார்க்கிறான்; காதுகளும் திறந்துள்ளன. ஆனால் அவனது <strong>மனம் எங்கோ மைதானத்திலோ விளையாட்டிலோ</strong> இருந்தால், அவனுக்கு ஒரு வார்த்தை கூடப் புரியாது!
                                இந்திரியங்களுக்குப் பின்னால் மனம் இருந்தால்தான் இந்திரியமே செயல்படும்.
                            </p>
                        </div>

                        <div class="base-card">
                            <h4 style="color:#06b6d4; margin-bottom:8px;"><i data-lucide="film"></i> உதாரணம் 2: சினிமா தியேட்டர் அனுபவம்</h4>
                            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                                விறுவிறுப்பான திரைப்படக் காட்சியில் மனம் முழுமையாக மூழ்கியிருக்கும்போது, திரையரங்கில் AC அணைக்கப்பட்டாலும் கூட, உடலின் <strong>வேர்வையோ அல்லது வெப்பமோ மனதை எட்டுவதே இல்லை!</strong>
                                ஏனெனில் மனம் புலன்களைத் தன் வசப்படுத்தி முழுமையாகக் காட்சியில் நிலைபெற்றுவிட்டது.
                            </p>
                        </div>
                    </div>

                    <!-- Doctor vs Thief Knife Paradigm -->
                    <div class="quote-callout" style="border-left-color:var(--saffron-primary); background:rgba(245,158,11,0.1); margin-top:20px;">
                        <h4 style="color:var(--saffron-primary); font-size:1.15rem; margin-bottom:8px;">
                            ⚖️ மருத்துவர் vs திருடன் கத்தி விவாதம் (The Doctor vs. Thief Knife Paradox)
                        </h4>
                        <p style="font-size:0.95rem; line-height:1.7;">
                            ஒரு <strong>மருத்துவரும் (Surgeon)</strong>, ஒரு <strong>திருடனும் (Thief)</strong> ஒரே மாதிரியான கூர்மையான கத்தியை எடுத்து மனித உடலைக் குத்தி கிழிக்கிறார்கள்.
                            உடலால் செய்யப்படும் <em>வெளிப்புறச் செயல் நூற்றுக்கு நூறு ஒன்றுதான்!</em><br>
                            • மருத்துவரின் மனதில் உள்ள நோக்கம்: <strong>உயிரைக் காப்பாற்ற வேண்டும், கட்டியை அகற்ற வேண்டும்</strong> ➔ புண்ணிய கர்மா (போற்றத்தக்க செயல்).<br>
                            • திருடனின் மனதில் உள்ள நோக்கம்: <strong>பணத்தைப் பறிக்க வேண்டும், காயப்படுத்த வேண்டும்</strong> ➔ கொடிய பாவ கர்மா (தண்டனைக்குரிய செயல்).<br>
                            <strong>முடிவுரை:</strong> கர்மாவைத் தீர்மானிப்பது வெறும் புற உடலின் உறுப்புகள் அல்ல; அதன் பின்னணியில் இயங்கும் <strong>மனதின் நோக்கமும் (Intention / சங்கல்பம்) எண்ணமுமே கர்மாவாகும்!</strong>
                        </p>
                    </div>
                </div>
            </section>

            <!-- ========================================== -->
            <!-- TOPIC 2: WHAT IS KARMA BANDHAM? (HOUR 2) -->
            <!-- ========================================== -->
            <section class="section-block" id="hour-2">
                <div class="section-title-wrap">
                    <span class="section-badge"><i data-lucide="link"></i> மணி 2 • இரண்டாம் அமர்வு (01:00 - 02:00)</span>
                    <h2 class="section-heading">2. கர்ம பந்தம் என்றால் என்ன? (What is Karma Bandham?) — 'நான்', 'எனது' மற்றும் எதிர்பார்ப்புச் சுமை</h2>
                    <p class="section-lead">
                        எந்தவொரு கர்மாவிலும் (செயலிலும்) தானாக எந்தக் குற்றமும் இல்லை; நெருப்பு சூடாக இருப்பதும், நீர் பாய்வதும் போல செயல்கள் இயற்கையானவை.
                        ஆனால் அச்செயலோடு <strong>பந்தம் (Bandham / Attachment)</strong> இணையும் போதுதான் மனிதன் துன்பத்திலும் கர்ம வினையிலும் சிறைப்படுகிறான்.
                        பந்தத்தின் இரு தூண்கள்: <strong>“நான்” (Ahankara / 'I')</strong> மற்றும் <strong>“எனது” (Mamakara / 'Mine')</strong> — இதன் பின்னால் இருப்பது காமம் (பேராசை & எதிர்பார்ப்பு).
                    </p>
                </div>

                <div class="base-card" style="border-left: 5px solid #ef4444; margin-bottom:24px;">
                    <h3 style="color:#ef4444; font-family:var(--font-heading); margin-bottom:8px;">
                        🚫 கர்மாவின் பெரும் பொய்: "நான் தனியாக இதைச் சாதித்துவிட்டேன்!"
                    </h3>
                    <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.7;">
                        இந்த பிரபஞ்சத்தில் எந்தவொரு தனி மனிதனாலும் <strong>தன்னந்தனியாக எதையுமே செய்துவிட முடியாது!</strong>
                        நாம் உண்ணும் ஒரு வாய் உணவு முதல் உடுத்தும் ஆடை வரை பிரபஞ்சத்தின் கோடிக்கணக்கான மனிதர்கள், விலங்குகள், இயற்கை பூதங்கள் இணைந்து சுமக்கும் கூட்டுழைப்பே ஆகும்.
                        அப்படி இருக்கையில் <em>“நான் சம்பாதித்தேன், எனது பணம், எனது சாப்பாடு”</em> என்று அகந்தை கொள்வது அறியாமையின் உச்சக்கட்டம்.
                    </p>
                </div>

                <!-- ACTIVITY 2.1: THE INFINITE WEB OF A GRAIN OF RICE -->
                <div class="activity-card-large" style="border-color:var(--saffron-primary);">
                    <div class="activity-header">
                        <div class="activity-title">
                            <i data-lucide="network" style="color:var(--saffron-primary);"></i>
                            செயல்பாடு 2.1: ஒரு பிடி சோற்றின் பிரபஞ்ச வலைப்பின்னல் (The Infinite Web of Every Grain of Rice)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="clock"></i> 25 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(16,185,129,0.15); color:#10b981;"><i data-lucide="share-2"></i> சார்புநிலை ஆய்வு</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>நோக்கம்:</strong> நாம் அன்றாடம் உண்ணும் தட்டில் உள்ள ஒரு கவளம் சோறு நம்மை வந்தடைவதற்கு எத்தனை மனிதர்கள் (மனுஷ்ய), இயற்கைச் சக்திகள் (பூத) மற்றும் விலங்குகள் (பசு/உயிரினங்கள்) தேவைப்படுகின்றன என்பதைச் சங்கிலித் தொடராகக் கண்டறிந்து பட்டியலிடுதல்.
                    </p>

                    <!-- Interactive Broken Link Simulator -->
                    <div class="interactive-widget">
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:14px;">
                            <h4 style="color:var(--saffron-primary); font-family:var(--font-heading);">
                                🌾 ஒரு பிடி சோற்றின் 16 கூட்டு ஆதரவுச் சங்கிலிகள் (கீழே கிளிக் செய்து சங்கிலியை உடைத்துச் சோதிக்கவும்)
                            </h4>
                            <button class="btn-timer" onclick="resetRiceChain()"><i data-lucide="refresh-cw"></i> அனைத்தையும் மீட்டமை</button>
                        </div>
                        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:12px;">
                            எந்தவொரு கட்டத்தின் மீதும் கிளிக் செய்தால் அச்சங்கிலி துண்டிக்கப்படும். உணவு நம்மை வந்தடையுமா என்பதைப் பாருங்கள்:
                        </p>

                        <div class="rice-chain-grid" id="rice-chain-container">
                            <!-- Generated by JS -->
                        </div>

                        <div id="rice-chain-status" style="margin-top:14px; padding:12px; border-radius:var(--radius-sm); background:rgba(16,185,129,0.12); color:#10b981; font-weight:700; font-size:0.9rem;">
                            ✅ அனைத்து 16 சங்கிலிகளும் இணைந்து இயங்குகின்றன — ஒரு பிடி சோறு உங்கள் தட்டிற்கு வெற்றிகரமாக வந்து சேர்கிறது!
                        </div>
                    </div>

                    <div class="debrief-box">
                        <strong>🎯 ஆழ்ந்த தத்துவப் போதனை:</strong><br>
                        மழை பெய்யாவிட்டால் (பூதம்), மண்புழு மண்ணை உழாவிட்டால், லாரி டிரைவர் வண்டி ஓட்டாவிட்டால், சிலிண்டர் விநியோகஸ்தர் வராவிட்டால், உப்பு காய்ச்சுபவர் இல்லாவிட்டால்... நாம் கோடீஸ்வரனாக இருந்தாலும் காகிதப் பணத்தைத் தின்ன முடியுமா?<br>
                        ஆகவே, <strong>“நான் உழைத்தேன், எனது சாப்பாடு”</strong> என்ற அகந்தை முற்றிலும் தவறானது. பிரபஞ்சத்திற்கு நாம் என்றும் கடமைப்பட்டிருக்கிறோம்!
                    </div>

                    <!-- Relationship Expectation Trap -->
                    <div class="card-grid-2" style="margin-top:20px;">
                        <div class="base-card" style="border-left:4px solid #ef4444;">
                            <h4 style="color:#ef4444; margin-bottom:6px;"><i data-lucide="heart-crack"></i> குடும்பத்தில் பந்தம் (எதிர்பார்ப்புச் சிறை)</h4>
                            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                                மனைவி, குழந்தைகள் மீது அன்பு செலுத்துவதில் தவறில்லை. ஆனால் <em>“நான் இவ்வளவு செய்தேன்; நீ எனக்கு பதிலுக்கு மரியாதை செய்ய வேண்டும், நான் சொல்வதைக் கேட்க வேண்டும்”</em> என்று கர்ம பலனைப் பிடித்துத் தொங்கும்போது ஏமாற்றமும், கோபமும், கர்ம பந்தமும் உருவாகிறது.
                            </p>
                        </div>
                        <div class="base-card" style="border-left:4px solid #10b981;">
                            <h4 style="color:#10b981; margin-bottom:6px;"><i data-lucide="shield-check"></i> விடுபடும் வழி (அன்பு செய், பலனை விடேன்)</h4>
                            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                                கடமையை முழுமையான அன்போடு 100% நேர்த்தியாகச் செய்ய வேண்டும். ஆனால் அதன் விளைவை (Karma Phalam) இறைவன் அல்லது காலத்தின் கைகளில் விட்டுவிட வேண்டும். அப்போது மனம் எந்நாளும் கலங்காத ஆனந்தத்தில் நிலைத்திருக்கும்.
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ========================================== -->
            <!-- TOPIC 3: DETAILING OF KARMA (HOUR 3) -->
            <!-- ========================================== -->
            <section class="section-block" id="hour-3">
                <div class="section-title-wrap">
                    <span class="section-badge"><i data-lucide="layers"></i> மணி 3 • மூன்றாம் அமர்வு (02:00 - 03:00)</span>
                    <h2 class="section-heading">3. ஷட் கருமங்களின் விரிவான விளக்கம் (Detailing of Karma) — 6 வகை கர்மாக்களின் துல்லிய ஆய்வு</h2>
                    <p class="section-lead">
                        சனாதன தர்மம் மனிதனின் அன்றாடச் செயல்பாடுகளை 6 துல்லியப் பிரிவுகளாகப் பிரிக்கிறது:
                        <strong>நித்ய, நைமித்திக, காம்ய, நிஷ்காம்ய, பிராயச்சித்த, மற்றும் நிஷித்த கர்மாக்கள்</strong>.
                        எந்தச் செயல் மனிதனை உயர்த்துகிறது, எது பந்தப்படுத்துகிறது, எதை அறவே தவிர்க்க வேண்டும் என்பதை அறிவதே விவேகம்.
                    </p>
                </div>

                <!-- 6 Karmas Detailed Cards Grid -->
                <div class="card-grid-3">
                    <div class="base-card" style="border-top: 4px solid var(--karma-nitya);">
                        <span class="badge-pill" style="background:var(--karma-nitya-bg); color:var(--karma-nitya); margin-bottom:8px;">1. கட்டாயக் கடமை</span>
                        <h3 style="color:var(--karma-nitya); font-family:var(--font-heading); margin-bottom:6px;">நித்ய கர்மா (Nitya)</h3>
                        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                            தினந்தோறும் தவறாமல் செய்ய வேண்டிய இன்றியமையாத கடமைகள். செய்தால் பாவம் இல்லை, செய்யாவிட்டால் பிரத்யவாய தோஷம் வரும் (எ.கா: காலை விழிப்பு, உடல்தூய்மை, சூரிய நமஸ்காரம், சந்தியாவந்தனம், பஞ்ச யக்ஞம்).
                        </p>
                    </div>

                    <div class="base-card" style="border-top: 4px solid var(--karma-naimittika);">
                        <span class="badge-pill" style="background:var(--karma-naimittika-bg); color:var(--karma-naimittika); margin-bottom:8px;">2. கால நிகழ்வுக் கடமை</span>
                        <h3 style="color:var(--karma-naimittika); font-family:var(--font-heading); margin-bottom:6px;">நைமித்திக கர்மா (Naimittika)</h3>
                        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                            குறிப்பிட்ட காரணங்களுக்காக அல்லது விசேஷ காலங்களில் செய்ய வேண்டிய கடமைகள் (எ.கா: அமாவாசை பித்ரு தர்ப்பணம், திதி சிரார்த்தம், தீபாவளி, பொங்கல், கிரகண ஸ்நானம், 16 சம்ஸ்கார சடங்குகள்).
                        </p>
                    </div>

                    <div class="base-card" style="border-top: 4px solid var(--karma-kamya);">
                        <span class="badge-pill" style="background:var(--karma-kamya-bg); color:var(--karma-kamya); margin-bottom:8px;">3. ஆசை சார்ந்த செயல்</span>
                        <h3 style="color:var(--karma-kamya); font-family:var(--font-heading); margin-bottom:6px;">காம்ய கர்மா (Kamya)</h3>
                        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                            தன் சுய ஆசை அல்லது குறிப்பிட்ட பலாபலன்களை எதிர்பார்த்துச் செய்யப்படும் விருப்பக் கர்மாக்கள் (எ.கா: பதவி உயர்வுக்கான வேள்வி, பரீட்சையில் முதல் மதிப்பெண் பெற அர்ச்சனை, வீடு கட்டும் நோன்பு).
                        </p>
                    </div>

                    <div class="base-card" style="border-top: 4px solid var(--karma-nishkamya);">
                        <span class="badge-pill" style="background:var(--karma-nishkamya-bg); color:var(--karma-nishkamya); margin-bottom:8px;">4. தன்னலமற்ற தியாகம்</span>
                        <h3 style="color:var(--karma-nishkamya); font-family:var(--font-heading); margin-bottom:6px;">நிஷ்காம்ய கர்மா (Nishkamya)</h3>
                        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                            எந்தவொரு சுய பலனையும் எதிர்பாராமல், லோக க்ஷேமத்திற்காகவும் இறை அர்ப்பணமாகவும் செய்யப்படும் தூய சேவை. இதுவே கர்ம பந்தங்களை அறுத்து சித்த சுத்தியையும் முக்தியையும் தரும் உன்னத வழி.
                        </p>
                    </div>

                    <div class="base-card" style="border-top: 4px solid var(--karma-prayaschitta);">
                        <span class="badge-pill" style="background:var(--karma-prayaschitta-bg); color:var(--karma-prayaschitta); margin-bottom:8px;">5. பரிகாரச் சுத்தி</span>
                        <h3 style="color:var(--karma-prayaschitta); font-family:var(--font-heading); margin-bottom:6px;">பிராயச்சித்த கர்மா (Prayaschitta)</h3>
                        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                            தெரிந்தோ தெரியாமலோ செய்த தவறுகள், பாபங்கள் மற்றும் குற்றங்களுக்கு உளப்பூர்வமாக வருந்தி, மனச்சுத்தி பெறச் செய்யும் பரிகாரங்கள் (எ.கா: விரதம், தானம், மன்னிப்பு கோருதல், மரம் நடுதல்).
                        </p>
                    </div>

                    <div class="base-card" style="border-top: 4px solid var(--karma-nishiddha);">
                        <span class="badge-pill" style="background:var(--karma-nishiddha-bg); color:var(--karma-nishiddha); margin-bottom:8px;">6. விலக்கப்பட்ட தீமைகள்</span>
                        <h3 style="color:var(--karma-nishiddha); font-family:var(--font-heading); margin-bottom:6px;">நிஷித்த கர்மா (Nishiddha)</h3>
                        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
                            சாஸ்திரங்களாலும் உலக தர்மத்தாலும் முற்றிலுமாகத் தடை செய்யப்பட்ட கொடிய தீய செயல்கள் (எ.கா: பிறரை வதைத்தல், களவு, பொய் சாட்சி, லஞ்சம், துரோகம், மது, வள்ளலாரின் 44 பாவங்கள்).
                        </p>
                    </div>
                </div>

                <!-- ACTIVITY 3.1: INTERACTIVE 12-SCENARIO KARMA CLASSIFICATION MATRIX -->
                <div class="activity-card-large">
                    <div class="activity-header">
                        <div class="activity-title">
                            <i data-lucide="check-square" style="color:var(--saffron-primary);"></i>
                            செயல்பாடு 3.1: கர்ம வகைப்பாட்டுப் போட்டி பலகை (12 Scenario Classification Challenge)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="clock"></i> 20 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(16,185,129,0.15); color:#10b981;"><i data-lucide="trophy"></i> ஊடாடும் வினாடி வினா</span>
                        </div>
                    </div>

                    <p style="margin-bottom:14px;">
                        கீழே உள்ள 12 நிஜ வாழ்க்கைச் சூழல்களைப் படித்து, அவை எந்தக் கர்மா வகையைச் சேர்ந்தவை எனச் சரியாகத் தேர்வு செய்யுங்கள். உடனடிப் புள்ளிகள் மற்றும் விளக்கத்தைப் பெறுங்கள்:
                    </p>

                    <!-- Interactive Quiz Area -->
                    <div class="interactive-widget" id="karma-matrix-box">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                            <span style="font-weight:800; color:var(--saffron-primary);">மதிப்பெண்: <span id="matrix-score">0</span> / 12 புள்ளிகள்</span>
                            <button class="btn-timer" onclick="resetKarmaMatrix()"><i data-lucide="rotate-ccw"></i> வினாடி வினா மீட்டமை</button>
                        </div>
                        <div id="karma-scenario-list" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:14px;">
                            <!-- Populated by JS -->
                        </div>
                    </div>
                </div>
            </section>

            <!-- ========================================== -->
            <!-- TOPIC 4: KARMA AS KARMA YOGA BY PANCHA MAHA YAGNAM (HOUR 4) -->
            <!-- ========================================== -->
            <section class="section-block" id="hour-4">
                <div class="section-title-wrap">
                    <span class="section-badge"><i data-lucide="flame"></i> மணி 4 • நான்காம் அமர்வு (03:00 - 04:15)</span>
                    <h2 class="section-heading">4. பஞ்ச மகா யக்ஞம் வழி கர்ம யோகம் (Karma as Karma Yoga by Pancha Maha Yagnam)</h2>
                    <p class="section-lead">
                        செயல் எவ்வாறு யோகமாக மாறுகிறது? தான் மட்டுமே வாழ வேண்டும் என்ற சுயநலத்திலிருந்து விடுபட்டு, தன்னுடைய உடலையும் செல்வத்தையும் அறிவையும் 5 பெரும் பிரபஞ்சக் கடமைகளாக அர்ப்பணிப்பதே கர்ம யோகம்!
                        இதற்காக நமது ரிஷிகள் வகுத்துக் கொடுத்ததே <strong>பஞ்ச மகா யக்ஞங்கள்</strong>.
                    </p>
                </div>

                <!-- ================= 4.1 PITRU YAGNAM ================= -->
                <div class="activity-card-large" style="border-color:#3b82f6;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:#3b82f6;">
                            <i data-lucide="users"></i>
                            4.1 பித்ரு யக்ஞம் &amp; நட்சத்திர நினைவுக் கட்ட செயல்முறை (Pitru Yagnam & The 5-Stage Life Star Matrix)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(59,130,246,0.15); color:#3b82f6;"><i data-lucide="clock"></i> 15 நிமிடங்கள்</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>செயல்முறை விளக்கம்:</strong> போர்டில் 5 வயதுப் பிரிவுகள் வரையப்பட்டுள்ளன (0-5 வயது | 5-10 வயது | 10-18 வயது | 18-60 வயது | 60 வயதுக்கு மேல்).
                        பயிற்சியில் உள்ள ஒவ்வொருவருக்கும் தலா 10 நட்சத்திரங்கள் (⭐) வழங்கப்படுகின்றன. உங்கள் வாழ்க்கையில் நடந்த நிகழ்வுகள் எந்த வயதில் உங்களுக்கு மிகவும் தெளிவாக நினைவிருக்கிறதோ அங்கு உங்கள் 10 நட்சத்திரங்களைப் பகிர்ந்து வைக்க வேண்டும்.
                    </p>

                    <!-- Interactive Star Board -->
                    <div class="star-board-wrap">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <h4 style="color:#3b82f6; font-family:var(--font-heading);">⭐ ஊடாடும் நட்சத்திர நினைவுக் கட்டப் பலகை</h4>
                            <span style="font-weight:700; font-size:0.85rem; color:var(--text-muted);">மீதமுள்ள நட்சத்திரங்கள்: <span id="stars-remaining" style="color:var(--saffron-primary); font-size:1.1rem; font-weight:800;">10</span></span>
                        </div>
                        <div class="star-columns-grid">
                            <div class="star-col">
                                <div class="star-col-title">0 - 5 வயது</div>
                                <div class="star-count-display" id="star-count-0">⭐ 0</div>
                                <div class="star-action-btns">
                                    <button class="btn-star-pm" onclick="changeStar(0, 1)">+</button>
                                    <button class="btn-star-pm" onclick="changeStar(0, -1)">-</button>
                                </div>
                                <small style="color:var(--text-dim); font-size:0.75rem;">குழந்தைப் பருவம்</small>
                            </div>
                            <div class="star-col">
                                <div class="star-col-title">5 - 10 வயது</div>
                                <div class="star-count-display" id="star-count-1">⭐ 1</div>
                                <div class="star-action-btns">
                                    <button class="btn-star-pm" onclick="changeStar(1, 1)">+</button>
                                    <button class="btn-star-pm" onclick="changeStar(1, -1)">-</button>
                                </div>
                                <small style="color:var(--text-dim); font-size:0.75rem;">பள்ளித் தொடக்கம்</small>
                            </div>
                            <div class="star-col">
                                <div class="star-col-title">10 - 18 வயது</div>
                                <div class="star-count-display" id="star-count-2">⭐ 3</div>
                                <div class="star-action-btns">
                                    <button class="btn-star-pm" onclick="changeStar(2, 1)">+</button>
                                    <button class="btn-star-pm" onclick="changeStar(2, -1)">-</button>
                                </div>
                                <small style="color:var(--text-dim); font-size:0.75rem;">இளமைப் பருவம்</small>
                            </div>
                            <div class="star-col">
                                <div class="star-col-title">18 - 60 வயது</div>
                                <div class="star-count-display" id="star-count-3">⭐ 6</div>
                                <div class="star-action-btns">
                                    <button class="btn-star-pm" onclick="changeStar(3, 1)">+</button>
                                    <button class="btn-star-pm" onclick="changeStar(3, -1)">-</button>
                                </div>
                                <small style="color:var(--text-dim); font-size:0.75rem;">செயல் வாழ்வு</small>
                            </div>
                            <div class="star-col">
                                <div class="star-col-title">> 60 வயது</div>
                                <div class="star-count-display" id="star-count-4">⭐ 0</div>
                                <div class="star-action-btns">
                                    <button class="btn-star-pm" onclick="changeStar(4, 1)">+</button>
                                    <button class="btn-star-pm" onclick="changeStar(4, -1)">-</button>
                                </div>
                                <small style="color:var(--text-dim); font-size:0.75rem;">முதுமைப் பருவம்</small>
                            </div>
                        </div>
                    </div>

                    <div class="debrief-box" style="border-color:#3b82f6; background:rgba(59,130,246,0.08);">
                        <strong style="color:#3b82f6;">🎯 வியப்பூட்டும் முடிவு & மனிதப் பிறவியின் உண்மை:</strong><br>
                        போர்டில் பார்த்தால் <strong>0-5 வயது மற்றும் >60 வயது கட்டங்கள் முற்றிலும் காலியாக அல்லது மிகக் குறைந்த நட்சத்திரங்களோடு இருக்கும்!</strong><br><br>
                        • <strong>மனிதன் பிறக்கும் போது வெறும் வன்பொருள் மட்டுமே (Born as Hardware without Software):</strong><br>
                        மனிதக் குழந்தைக்குப் பிறக்கும்போது எச்சில் துப்பத் தெரியாது, மலம் கழிக்கத் தெரியாது, நடக்கவோ பேசவோ தெரியாது. பெற்றோர் இரவு பகல் பாராமல் தன் மடியில் சுமந்து, மலம் அள்ளி, உணவூட்டி மென்பொருளை (Software) ஏற்றுகிறார்கள்.<br><br>
                        • <strong>விலங்கு உலகத்தோடு ஒப்பிடுங்கள்:</strong><br>
                        - பூனை (Cat): 6 முதல் 8 வாரங்கள் மட்டுமே குட்டியைப் பராமரிக்கும்; பின் பிரிந்துவிடும்.<br>
                        - நாய் (Dog): 7 முதல் 8 வாரங்களில் குட்டியைத் தானாகத் திரிய விட்டுவிடும்.<br>
                        - கழுகு (Eagle): 10 முதல் 12 வாரங்களில் கூட்டிலிருந்து வெளியே தள்ளிவிடும்.<br>
                        - குதிரை (Horse): பிறந்த 1 முதல் 2 மணி நேரத்திலேயே எழுந்து ஓடத் தொடங்கும்!<br>
                        - யானை (Elephant): 3 முதல் 5 ஆண்டுகள் வரை மட்டுமே தாயுடன் இருக்கும்.<br>
                        <strong>ஆனால் மனிதன் மட்டுமே தன் குழந்தையை 25 ஆண்டுகள், ஏன் தன் வாழ்நாள் இறுதி வரை கண்ணின் இமைபோல் காக்கிறான்!</strong><br><br>
                        • <strong>இரண்டாம் குழந்தைப் பருவம் (>60 வயது):</strong><br>
                        60-70 வயதுக்கு மேல் பெற்றோரின் உடலும் மனமும் மீண்டும் 0-5 வயதுக் குழந்தையாகவே மாறி நினைவுகள் மங்கிச் சுருங்கி விடுகின்றன.
                        குழந்தையாய் இருந்த நம்மைப் பெற்றோர்கள் காப்பாற்றியது போல, முதுமையில் குழந்தையாக மாறும் பெற்றோரைப் பாதுகாப்பதே நமது முதன்மையான <strong>பித்ரு யக்ஞமாகும் (Pitru Yagnam)</strong>!
                    </div>
                </div>

                <!-- ================= 4.2 BHUTA YAGNAM ================= -->
                <div class="activity-card-large" style="border-color:#10b981;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:#10b981;">
                            <i data-lucide="trees"></i>
                            4.2 பூத யக்ஞம் &amp; இயற்கையின் 10 கண்ணுக்குத் தெரியாத கொடைகள் (Bhuta Yagnam & The 10 Ecological Debts)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(16,185,129,0.15); color:#10b981;"><i data-lucide="clock"></i> 15 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="globe"></i> 10 மில்லியன் உயிரினங்கள்</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        நாம் சுவாசிக்கும் ஒவ்வொரு மூச்சிலும் பருகும் ஒவ்வொரு சொட்டு நீரிலும் இயற்கையின் பல்லாயிரம் உயிரினங்கள் நமக்கு ஓயாது சேவை செய்கின்றன. நாம் அவற்றைத் துன்புறுத்தினாலும் அவை நமக்கு நன்மையே செய்கின்றன:
                    </p>

                    <!-- 10 Invisible Gifts Grid -->
                    <div class="card-grid-2">
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">1. மரங்கள் (Trees): CO2 உட்கொண்டு O2 தருதல்</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">மனிதன் வெளியேற்றும் நச்சு கரியமில வாயுவை உறிஞ்சி, மனித குலம் வாழ பிராண வாயுவை (Oxygen) இலவசமாகத் தருகின்றன.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">2. தேனீக்கள் (Bees): அயல் மகரந்தச் சேர்க்கை</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">பூக்களிடையே மகரந்தத்தைச் சுமந்து பயிர்களைப் பெருக்குகின்றன. தேனீக்கள் அழிந்தால் மனித குலம் 4 ஆண்டுகளில் பட்டினியால் அழியும்!</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">3. பறவைகள் (Birds): விதைகளைப் பரப்புதல்</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">காட்டுப் பழங்களைத் தின்று மலைகளிலும் காடுகளிலும் எச்சமிட்டு அடர்ந்த காடுகளை உருவாக்குகின்றன.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">4. சூரியன் &amp; பெருங்கடல் (Sun & Sea): மழைச் சுழற்சி</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">குடிக்க முடியாத உப்புநீரை ஆவியாக்கி, மேகங்களாக்கி, தித்திக்கும் நன்னீராக மழையாகப் பொழிகின்றன.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">5. மண்புழுக்கள் (Earthworms): நிலத்தின் உழவர்கள்</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">மண்ணைத் தின்று செரித்து, பூமிக்குள் துளையிட்டு காற்றோட்டம் தந்து, உலகிலேயே சிறந்த இயற்கை உரத்தை உருவாக்குகின்றன.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">6. அலையாத்திக் காடுகள் (Mangroves): சுனாமி அரண்</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">ஆழ்கடலின் ராட்சத அலைகளையும் சுனாமியையும் தடுத்து கடற்கரை ஊர்களைக் காக்கும் இயற்கை மதில்சுவர்.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">7. பசு &amp; காளை (Cow & Bullock): அமுதப் பால் &amp; உரம்</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">புல்லைத் தின்று மனிதனுக்கு அமிர்தமாகப் பால் தருகிறது; சாணமும் கோமியமும் பூமியை மலடாக்காமல் காக்கும் பஞ்சகவ்யம்.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">8. ஆறுகள் (Rivers): வண்டல் மண் &amp; நாகரிகம்</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">இமயத்திலும் மேற்குத் தொடர்ச்சி மலையிலும் தோன்றி தாதுக்கள் நிறைந்த வண்டல் மண்ணைச் சுமந்து வந்து சோறூட்டுகின்றன.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">9. நுண்ணுயிரிகள் (Microbes & Fungi): கழிவுச் சிதைவு</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">இறந்த இலைகள், குப்பைகளை மக்கச்செய்து மீண்டும் உரமாக மாற்றி பூமியை நாற்றமெடுக்காமல் தூய்மைப்படுத்துகின்றன.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:8px;">10. ஓசோன் படலம் (Ozone Layer): கதிர்வீச்சுப் பாதுகாப்பு</h4>
                            <p style="font-size:0.86rem; color:var(--text-muted);">விண்ணிலிருந்து வரும் கொடிய புற ஊதாக் கதிர்களிடமிருந்து (UV rays) பூமியில் உள்ள அனைத்து ஜீவராசிகளையும் காக்கும் குடை.</p>
                        </div>
                    </div>

                    <!-- Ancient Reverence vs Modern Exploitation -->
                    <div class="quote-callout" style="border-left-color:#10b981; background:rgba(16,185,129,0.08); margin-top:20px;">
                        <h4 style="color:#10b981; font-size:1.1rem; margin-bottom:8px;">
                            🏛️ பண்டைய பாரதத்தின் பூத மரியாதை vs நவீனச் சுரண்டல்:
                        </h4>
                        <p style="font-size:0.95rem; line-height:1.7;">
                            • <strong>மரம் வெட்டும் சடங்கு:</strong> முற்காலத்தில் கோயில் அல்லது வாழ்வாதாரத்திற்கு ஒரு மரத்தை வெட்ட வேண்டியிருந்தால் கூட, முதலில் அந்த மரத்திடம் மன்னிப்பு வேண்டிப் பிரார்த்தித்து, 5 முதல் 10 மரக்கன்றுகளை நட்டு, அவை ஒரு மனித உயரம் வளரும் வரை காத்திருந்து பின்னரே அந்த ஒரு மரத்தை வெட்டுவார்கள்!<br>
                            • <strong>ஆவுரஞ்சிக் கல் (Cow Rubbing Stone):</strong> மாடுகள் தனது கழுத்திலும் முதுகிலும் ஏற்படும் அரிப்பைப் போக்கிக் கொள்ள வழியெங்கும் <em>'ப' வடிவக் கற்களை</em> நட்டு வைத்த தமிழர்களின் கருணையை எண்ணிப் பாருங்கள்!<br>
                            • <strong>திருக்கோயில் குளங்கள்:</strong> ஊரெங்கும் நிலத்தடி நீரைச் சேமித்து சகல உயிர்களுக்கும் தாகம் தீர்த்தன.<br>
                            👉 <strong>பூத யக்ஞ உறுதிமொழி:</strong> பூமி மனிதனுக்கு மட்டுமே சொந்தமானது அல்ல; 10 மில்லியன் வகை உயிரினங்களுக்கும் (84 லட்சம் ஜீவராசிகள்) சொந்தமானது. நீரை வீணாக்க மாட்டோம், பிளாஸ்டிக் எறிய மாட்டோம், பறவைகளுக்கும் எறும்புகளுக்கும் உணவிடுவோம், மரங்களை நடுவோம்!
                        </p>
                    </div>
                </div>

                <!-- ================= 4.3 NARA / MANUSHYA YAGNAM ================= -->
                <div class="activity-card-large" style="border-color:#f59e0b;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:var(--saffron-primary);">
                            <i data-lucide="handshake"></i>
                            4.3 நர / மனுஷ்ய யக்ஞம்: மனித ஆதரவுச் சங்கிலி விவாதம் (Human Support Chain Challenge)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="clock"></i> 15 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(59,130,246,0.15); color:#3b82f6;"><i data-lucide="users"></i> இரு அணிகள் போட்டி</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>விளையாட்டு முறை:</strong> அரங்கம் இரண்டு அணிகளாகப் பிரிக்கப்படுகிறது (அணி 'அ' & அணி 'ஆ').
                        அணி 'அ' சமுதாயத்தில் உள்ள ஒரு தொழிலாளி/மனிதரின் பெயரைக் கூற வேண்டும் (எ.கா: <em>ஆசிரியர்</em>).
                        அணி 'ஆ' அவர் மனித குலத்திற்குச் செய்யும் நன்மையை உடனே கூற வேண்டும் (எ.கா: <em>அறிவையும் ஒழுக்கத்தையும் புகட்டுகிறார்</em>).
                        பின் அணி 'ஆ' அடுத்த மனிதரைக் கூறும் (எ.கா: <em>துப்புரவுப் பணியாளர்</em>); அணி 'அ' அதற்கான நன்மையைச் சொல்லும் (எ.கா: <em>குப்பைகளை அகற்றி தொற்றுநோய் வராமல் நம்மைக் காப்பவர்</em>).
                        ஒரு அணி விடையளிக்கத் திணறும் வரை சங்கிலி தொடரும்!
                    </p>

                    <!-- Interactive Score Keeper -->
                    <div class="interactive-widget">
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                            <h4 style="color:var(--saffron-primary); font-family:var(--font-heading);">
                                📋 நர யக்ஞ நேரடி விவாதப் பலகை (Live Match Logger)
                            </h4>
                            <div style="display:flex; gap:10px;">
                                <button class="btn-timer" onclick="addNaraChainItem()"><i data-lucide="plus"></i> புதிய தொழில் சேர்</button>
                                <button class="btn-timer" onclick="resetNaraChain()"><i data-lucide="rotate-ccw"></i> மீட்டமை</button>
                            </div>
                        </div>
                        <div id="nara-chain-list" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px;">
                            <!-- Populated by JS -->
                        </div>
                    </div>

                    <div class="debrief-box">
                        <strong>🎯 தத்துவ முடிவு:</strong><br>
                        போர்டில் நூற்றுக்கணக்கான மனிதர்களின் பெயர்கள் நிறையும் போது நாம் உணர்வது: <strong>நாம் யாருமே தற்சார்பு கொண்ட தனித்தீவுகள் அல்ல!</strong>
                        விவசாயி, டிரைவர், தையல்காரர், மருத்துவர், ராணுவ வீரர், எலக்ட்ரீசியன் என சமுதாயமே நம்மைத் தாங்குகிறது.
                        எனவே சக மனிதர்களிடம் கடுகடுப்பின்றி <strong>கருணை (Karunai)</strong>, புன்னகை, இன்சொல், நியாயமான ஊதியம், அதிதி உபசரிப்பு செய்வதே மனுஷ்ய யக்ஞம்!
                    </div>
                </div>

                <!-- ================= 4.4 RISHI YAGNAM ================= -->
                <div class="activity-card-large" style="border-color:#8b5cf6;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:#8b5cf6;">
                            <i data-lucide="scroll"></i>
                            4.4 ரிஷி யக்ஞம்: பாரதத்தின் 200 ரிஷிகள் &amp; நைமிசாரண்ய மகா சபை (Rishi Yagnam & The 200 Rishis Repository)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(139,92,246,0.15); color:#8b5cf6;"><i data-lucide="clock"></i> 20 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(16,185,129,0.15); color:#10b981;"><i data-lucide="book-open"></i> 200 ரிஷிகள் களஞ்சியம்</span>
                        </div>
                    </div>

                    <!-- Naimisharanya Teaching -->
                    <div class="quote-callout" style="border-left-color:#8b5cf6; background:rgba(139,92,246,0.08);">
                        <h4 style="color:#8b5cf6; font-size:1.15rem; margin-bottom:8px;">
                            🌲 நைமிசாரண்யத்தில் 100 ஆண்டுகளுக்கு ஒருமுறை கூடிய முனிவர்கள் மாநாடு:
                        </h4>
                        <p style="font-size:0.95rem; line-height:1.7;">
                            பண்டைய பாரதத்தில் ஒவ்வொரு 100 ஆண்டுகளுக்கும் ஒருமுறை பாரதத்தின் நான்கு மூலைகளிலிருந்தும் பல்லாயிரக்கணக்கான ரிஷிகள் <strong>நைமிசாரண்யம்</strong> (Naimisharanya) புனிதக் காட்டில் ஒன்று கூடுவார்கள்.
                            சௌனக மகரிஷி, சூத பௌராணிகர், வியாசர் தலைமையில் கூடி கால மாற்றங்களை விவாதித்து சமுதாய ஒழுங்கை வகுப்பார்கள்.<br>
                            நாம் கொண்டாடும் <strong>தீபாவளி, பொங்கல், சிவராத்திரி, நவராத்திரி, திருக்கோயில் திருவிழாக்கள்</strong>, இல்லற தர்மம் மற்றும் மனிதனின் பிறப்பு முதல் இறப்பு வரையிலான <strong>16 சம்ஸ்காரங்கள் (16 Rites of Passage)</strong> அனைத்தும் அந்த ரிஷிகள் கூடித் திட்டமிட்டுக் கொடுத்த கொடையே ஆகும்!<br>
                            இன்று நாம் அமைதியாகக் கூடி தர்மத்தைப் பேசுகிறோம் என்றால் அது அவர்கள் செய்த கடும் தவத்தின் பலனே.
                            <strong>ரிஷி யக்ஞம் என்பது:</strong> ஏதேனும் 1 அல்லது 2 ரிஷிகளின் போதனைகளைத் தேர்ந்தெடுத்து, படித்து, நம் வாழ்க்கையில் நடைமுறைப்படுத்துவதே ஆகும்!
                        </p>
                    </div>

                    <!-- 200 Rishis Interactive Database -->
                    <div class="interactive-widget" style="margin-top:20px;">
                        <div class="rishi-toolbar">
                            <div class="search-input-box">
                                <i data-lucide="search"></i>
                                <input type="text" id="rishi-search-box" placeholder="ரிஷியின் பெயர் அல்லது பங்களிப்பைத் தேடுக (Search by Name or Wisdom)..." oninput="filterRishis()">
                            </div>
                            <span style="font-size:0.85rem; font-weight:700; color:var(--saffron-primary);" id="rishi-counter-text">
                                காண்கிறது: 200 / 200 ரிஷிகள்
                            </span>
                        </div>

                        <!-- Category Filter Pills -->
                        <div class="category-pill-group" id="rishi-cat-pills">
                            <button class="btn-cat-pill active" onclick="setRishiCategory('all', this)">அனைத்தும் (All 200)</button>
                            <button class="btn-cat-pill" onclick="setRishiCategory('saptarishi', this)">சப்தரிஷிகள் &amp; பிரஜாபதிகள்</button>
                            <button class="btn-cat-pill" onclick="setRishiCategory('vedic', this)">வேத ரிஷிகள்</button>
                            <button class="btn-cat-pill" onclick="setRishiCategory('rishika', this)">வேத ரிஷிகைகள் (பெண் ஞானிகள்)</button>
                            <button class="btn-cat-pill" onclick="setRishiCategory('upanishad', this)">உபநிடத ரிஷிகள்</button>
                            <button class="btn-cat-pill" onclick="setRishiCategory('siddha', this)">18 தமிழ் சித்தர்கள் &amp; அருளாளர்கள்</button>
                            <button class="btn-cat-pill" onclick="setRishiCategory('shastra', this)">சாஸ்திர &amp; விஞ்ஞானிகள்</button>
                        </div>

                        <!-- Rishi Scroll Cards Container -->
                        <div class="rishi-list-scroll" id="rishi-list-container">
                            <!-- Populated by JS -->
                        </div>

                        <!-- Pick 2 Rishis Generator Tool -->
                        <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-sm); padding:16px; margin-top:16px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
                            <div>
                                <h4 style="color:var(--saffron-primary); font-size:1rem; margin-bottom:4px;">🌟 என் வாழ்விற்கான 2 வழிகாட்டி ரிஷிகள் (My 2 Guiding Rishis)</h4>
                                <p style="font-size:0.82rem; color:var(--text-muted);">ஏதேனும் இரண்டு ரிஷிகளைத் தேர்ந்தெடுத்து வாழ்க்கையில் அவர்கள் கொள்கையைக் கடைப்பிடிக்க உறுதி எடுங்கள்.</p>
                            </div>
                            <button class="btn-timer btn-timer-primary" onclick="randomPickTwoRishis()">
                                <i data-lucide="sparkles"></i> எனக்குரிய 2 ரிஷிகளைப் பரிந்துரை செய்
                            </button>
                        </div>
                        <div id="picked-rishis-display" style="display:none; margin-top:12px; padding:14px; border-radius:var(--radius-sm); background:rgba(139,92,246,0.12); border:1px solid #8b5cf6;">
                            <!-- Populated when clicked -->
                        </div>
                    </div>
                </div>

                <!-- ================= 4.5 DEIVA YAGNAM ================= -->
                <div class="activity-card-large" style="border-color:#06b6d4;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:#06b6d4;">
                            <i data-lucide="sun-medium"></i>
                            4.5 தெய்வ யக்ஞம்: சிவபுராண பாராயணம், உடலின் அற்புதம் &amp; பிரபஞ்ச ஜூம் (Deiva Yagnam & The Cosmic Wonder)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(6,182,212,0.15); color:#06b6d4;"><i data-lucide="clock"></i> 20 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(245,158,11,0.15); color:var(--saffron-primary);"><i data-lucide="star"></i> தத்துவமசி</span>
                        </div>
                    </div>

                    <!-- Shiva Puranam Group Chanting -->
                    <div class="quote-callout" style="border-left-color:#06b6d4; background:rgba(6,182,212,0.08);">
                        <h4 style="color:#06b6d4; font-size:1.15rem; margin-bottom:8px;">
                            🕉️ மாணிக்கவாசகரின் சிவபுராண கூட்டுப் பாராயணம் (அனைவரும் இணைந்து ஓதுதல்):
                        </h4>
                        <p style="font-size:1.05rem; line-height:1.9; font-family:var(--font-heading); color:var(--text-main);">
                            “புல்லாகிப் பூடாய்ப் புழுவாய் மரமாகிப்<br>
                            பல்விருக மாகிப் பறவையாய்ப் பாம்பாகிக்<br>
                            கல்லாய் மனிதராய்ப் பேயாய்க் கணங்களாய்<br>
                            வல்லசுர ராகி முனிவராய்த் தேவராய்ச்<br>
                            செல்லாஅ நின்றஇத் தாவர சங்கமத்துள்<br>
                            எல்லாப் பிறப்பும் பிறந்திளைத்தேன் எம்பெருமான்<br>
                            மெய்யேஉன் பொன்னடிகள் கண்டின்று வீடுற்றேன்!”
                        </p>
                        <p style="font-size:0.88rem; color:var(--text-dim); margin-top:8px;">
                            <em>விளக்கம்:</em> புல், செடி, புழு, மரம், பல்வேறு விலங்குகள், பறவை, பாம்பு, கல், மனிதர் என 84 லட்சம் யோனிப் பிறவிகளிலும் பிறந்து இளைத்த எனக்கு, மெய்யான மனிதப் பிறவியையும் நற்புத்தியையும் தந்த இறைவா, உன் பொன்னடிகளைச் சரணடைந்து முக்தி அடைகிறேன்!
                        </p>
                    </div>

                    <!-- Complex Human Body Miracle -->
                    <div class="interactive-widget">
                        <h4 style="color:var(--saffron-primary); font-family:var(--font-heading); margin-bottom:8px;">
                            🫀 உடலின் உள்ளே நடக்கும் தானியங்கி அற்புதங்கள் (The Involuntary Miracle Engine)
                        </h4>
                        <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:14px;">
                            நம் உடலில் நடக்கும் கணக்கற்ற இயக்கங்களில் ஏதேனும் ஒன்றை 'நான்' செய்கிறேனா?
                        </p>
                        <div class="card-grid-4">
                            <div class="base-card">
                                <h5 style="color:#ef4444;"><i data-lucide="heart"></i> இரத்த ஓட்ட மண்டலம்</h5>
                                <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">இதயம் தினமும் 1,00,000 முறை தானாகவே துடிக்கிறது. நாம் தூங்கினாலும் ஒரு நொடி நிற்காது.</p>
                            </div>
                            <div class="base-card">
                                <h5 style="color:#f59e0b;"><i data-lucide="utensils"></i> செரிமான மண்டலம்</h5>
                                <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">நாம் விழுங்கும் சோற்றை இரத்தமாகவும் சதையாகவும் எலும்பாகவும் மாற்றும் அமில ரசவாதம் தானாக நடக்கிறது.</p>
                            </div>
                            <div class="base-card">
                                <h5 style="color:#8b5cf6;"><i data-lucide="activity"></i> நரம்பு மண்டலம்</h5>
                                <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">வினாடிக்கு கோடிக்கணக்கான மின் சமிக்ஞைகளை மூளை அனுப்பி உடலை இயக்குகிறது.</p>
                            </div>
                            <div class="base-card">
                                <h5 style="color:#06b6d4;"><i data-lucide="droplet"></i> கழிவுநீக்க மண்டலம்</h5>
                                <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">சிறுநீரகங்கள் தினமும் 180 லிட்டர் இரத்தத்தைச் சுத்திகரித்து நச்சை வெளியேற்றுகின்றன.</p>
                            </div>
                        </div>
                        <p style="font-size:0.92rem; color:var(--text-main); font-weight:700; margin-top:14px; text-align:center;">
                            👉 இதில் எதையாவது 'நான்' இயக்குகிறேனா? இல்லை! அனைத்தும் பிரபஞ்ச சக்தியின் இயக்கம். பிறகு எதற்கு இந்த வீண் கர்வம்?
                        </p>
                    </div>

                    <!-- Cosmic Zoom Out Explorer -->
                    <div class="interactive-widget" style="margin-top:20px;">
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                            <h4 style="color:#06b6d4; font-family:var(--font-heading);">
                                🌌 பிரபஞ்ச அளவுகோல் ஜூம்: "நாம் தூசு கூட அல்ல!" (Cosmic Scale Explorer)
                            </h4>
                            <span style="font-size:0.85rem; color:var(--text-dim);">நிலையை நகர்த்தி பிரபஞ்சப் பிரம்மாண்டத்தைக் காண்க</span>
                        </div>
                        <input type="range" min="1" max="8" value="1" id="cosmic-slider" oninput="updateCosmicScale(this.value)" style="width:100%; accent-color:#06b6d4; margin-bottom:14px;">
                        
                        <div id="cosmic-display-card" class="base-card" style="text-align:center; padding:24px; border:2px solid #06b6d4; background:rgba(6,182,212,0.06);">
                            <div style="font-size:2.4rem; margin-bottom:8px;" id="cosmic-icon">🏛️</div>
                            <h3 style="font-family:var(--font-heading); color:#06b6d4; margin-bottom:6px;" id="cosmic-title">நிலை 1: இந்தப் பயிற்சி அரங்கம் (This Workshop Hall)</h3>
                            <p style="font-size:0.95rem; color:var(--text-muted); max-width:700px; margin:0 auto;" id="cosmic-desc">
                                நாம் தற்போது அமர்ந்திருக்கும் சில நூறு சதுர அடி அறை. இங்கு அமர்ந்து கொண்டு நாம் நம்மைப் பேரறிவாளியாக நினைக்கிறோம்.
                            </p>
                        </div>
                    </div>

                    <div class="debrief-box" style="border-color:#06b6d4; background:rgba(6,182,212,0.08); margin-top:20px;">
                        <strong style="color:#06b6d4;">🎯 தெய்வ யக்ஞம் &amp; தத்துவமசி (Tat Tvam Asi):</strong><br>
                        1. தினமும் 1 நிமிடம் அமைதியாக அமர்ந்து இந்த பிரபஞ்ச சக்தியை மனதார நன்றியோடு நினையுங்கள்.<br>
                        2. <strong>“தத்துவமசி”</strong> — இந்த அண்டத்தில் பரவியுள்ள அதே பரம்பொருளின் ஒரு நுண்ணிய ஒளிக் கீற்றே எனக்குள்ளும் ஆத்மாவாக ஒளிர்கிறது என்பதை உணர்வதே மெய்ஞானம்!
                    </div>
                </div>
            </section>

            <!-- ========================================== -->
            <!-- TOPIC 5: SLOWLY PRACTICE NISHKAMYA (HOUR 5) -->
            <!-- ========================================== -->
            <section class="section-block" id="hour-5">
                <div class="section-title-wrap">
                    <span class="section-badge"><i data-lucide="award"></i> மணி 5 • நிறைவு அமர்வு (04:15 - 05:00)</span>
                    <h2 class="section-heading">5. சுயநலமற்ற நிஷ்காமியப் பயிற்சி (Slowly Practice Nishkamya) — 4 ஆசிரமப் படிகள் &amp; நிறைவுச் சங்கல்பம்</h2>
                    <p class="section-lead">
                        ஒரே நாளில் எவரும் ஞானியாகி விட முடியாது; குழந்தை மெல்ல நடை பழகுவது போல, மனிதன் தன் வாழ்க்கையை 4 பருவங்களாகப் பிரித்து,
                        சுயநலத்தை மெல்ல மெல்ல உருக்கி, அனைத்தையும் தழுவும் பேரன்பாக விரிவடைய வேண்டும்.
                    </p>
                </div>

                <!-- 4 Ashrama Stages Cards -->
                <div class="card-grid-4">
                    <div class="base-card" style="border-top:4px solid #10b981;">
                        <span class="badge-pill" style="background:var(--karma-nitya-bg); color:#10b981; margin-bottom:6px;">படி 1</span>
                        <h4 style="color:#10b981; font-family:var(--font-heading);">பிரம்மச்சர்யம் (Brahmacharya)</h4>
                        <p style="font-size:0.84rem; color:var(--text-muted); margin-top:6px;">
                            கல்வி, ஒழுக்கம், புலனடக்கம், குருபக்தி மற்றும் உடல்திறன் வளர்க்கும் இளமைப் பருவம்.
                        </p>
                    </div>

                    <div class="base-card" style="border-top:4px solid var(--saffron-primary);">
                        <span class="badge-pill" style="background:var(--karma-kamya-bg); color:var(--saffron-primary); margin-bottom:6px;">படி 2</span>
                        <h4 style="color:var(--saffron-primary); font-family:var(--font-heading);">கிரஹஸ்தம் (Grihastha)</h4>
                        <p style="font-size:0.84rem; color:var(--text-muted); margin-top:6px;">
                            இல்லறம் — தன் சுயநலத்தை உருக்கும் உலைக்களம்! மனைவி, குழந்தைகள், பெற்றோருக்காகத் தியாகம் செய்து 'நான்' என்பதை விரிக்கும் களம்.
                        </p>
                    </div>

                    <div class="base-card" style="border-top:4px solid #3b82f6;">
                        <span class="badge-pill" style="background:var(--karma-naimittika-bg); color:#3b82f6; margin-bottom:6px;">படி 3</span>
                        <h4 style="color:#3b82f6; font-family:var(--font-heading);">வானபிரஸ்தம் (Vanaprastha)</h4>
                        <p style="font-size:0.84rem; color:var(--text-muted); margin-top:6px;">
                            உலகியல் பற்றுகளைத் தளர்த்தி, அடுத்த தலைமுறைக்கு வழிகாட்டி, தியானத்திலும் சமுதாயப் பொதுப்பணியிலும் ஈடுபடுதல்.
                        </p>
                    </div>

                    <div class="base-card" style="border-top:4px solid #8b5cf6;">
                        <span class="badge-pill" style="background:var(--karma-nishkamya-bg); color:#8b5cf6; margin-bottom:6px;">படி 4</span>
                        <h4 style="color:#8b5cf6; font-family:var(--font-heading);">சன்யாசம் (Sannyasa)</h4>
                        <p style="font-size:0.84rem; color:var(--text-muted); margin-top:6px;">
                            அகில உலக அன்பு; சர்வ ஜீவ தயவு; அனைத்தும் இறைவனின் வடிவம் என உணர்ந்து பந்தங்களற்ற முழு முக்தி நிலை.
                        </p>
                    </div>
                </div>

                <!-- Family as Crucible Quote -->
                <div class="quote-callout" style="border-left-color:var(--saffron-primary); background:rgba(245,158,11,0.08); margin:24px 0;">
                    <h4 style="color:var(--saffron-primary); font-size:1.15rem; margin-bottom:6px;">
                        🏡 குடும்பம்: சுயநலத்தை உருக்கும் ஆன்மீக உலைக்களம் (Family as the Divine Crucible)
                    </h4>
                    <p style="font-size:0.95rem; line-height:1.7;">
                        காட்டுக்குச் சென்று தவம் செய்வதை விட, இல்லறத்தில் வாழ்வதே சுயநலத்தை ஒழிப்பதற்கான சிறந்த பயிற்சியாகும்.
                        குழந்தைக்காகத் தன் தூக்கத்தைத் தியாகம் செய்கிறான்; குடும்பத்திற்காகத் தன் உணவைத் தியாகம் செய்கிறான்.
                        இவ்வாறாக <strong>நான் ➔ குடும்பம் ➔ சமுதாயம் ➔ தேசம் ➔ அகில பிரபஞ்சம்</strong> என நமது அன்பின் எல்லை படிப்படியாக விரிய வேண்டும்!
                    </p>
                </div>

                <!-- ACTIVITY 5.1: BALLOON / PAPER ARPANAM SIMULATOR -->
                <div class="activity-card-large" style="border-color:#ef4444;">
                    <div class="activity-header">
                        <div class="activity-title" style="color:#ef4444;">
                            <i data-lucide="cloud-rain"></i>
                            செயல்பாடு 5.1: ஈஸ்வர சமர்ப்பண பலூன் / காகிதப் பற்று நீக்கும் செயல்முறை (The Balloon / Paper Release of Ego)
                        </div>
                        <div class="activity-meta">
                            <span class="badge-pill" style="background:rgba(239,68,68,0.15); color:#ef4444;"><i data-lucide="clock"></i> 15 நிமிடங்கள்</span>
                            <span class="badge-pill" style="background:rgba(16,185,129,0.15); color:#10b981;"><i data-lucide="feather"></i> பற்றற்ற விடுதலை</span>
                        </div>
                    </div>

                    <p style="margin-bottom:12px;">
                        <strong>நேரடிப் பயிற்சி முறை:</strong> பங்கேற்பாளர்கள் அனைவருக்கும் ஒரு பலூன் அல்லது காகிதத் துண்டு தரப்படுகிறது.
                        அதில் தன் மனதை வாட்டும் <em>அகந்தை, கோபம், பிறர் பாராட்ட வேண்டும் என்ற எதிர்பார்ப்பு, தோல்வி பயம்</em> ஆகியவற்றை எழுதிக் கொள்கிறார்கள்.
                        அதை இறுக்கமாகக் கைகளில் பிடித்திருக்கும் வரை கைகள் அடைபட்டிருக்கும்; எவருக்கும் சேவை செய்ய முடியாது.
                        அதை வானில் விடுவிக்கும் போது அல்லது <strong>சமர்ப்பண குண்டத்தில் (Arpana Kundam)</strong> இடும் போது கைகள் விடுபடுகின்றன!
                    </p>

                    <!-- Interactive Balloon Release Simulator -->
                    <div class="balloon-stage">
                        <div class="divine-light-glow"></div>
                        <div class="floating-balloon" id="interactive-balloon">
                            <span id="balloon-text">நான் &amp; எனது</span>
                        </div>
                        <div style="margin-top:20px; z-index:10; display:flex; gap:10px; width:100%; max-width:480px;">
                            <input type="text" id="ego-input" placeholder="உங்கள் பற்று/சுமையை உள்ளிடுக (எ.கா: பாராட்டு ஆசை, கோபம்)..." style="flex:1; padding:8px 12px; border-radius:var(--radius-sm); border:1px solid var(--border-color); background:var(--bg-card); color:var(--text-main); font-size:0.85rem;">
                            <button class="btn-timer btn-timer-primary" onclick="releaseBalloon()"><i data-lucide="send"></i> சமர்ப்பணம் செய்</button>
                        </div>
                        <small style="color:var(--text-dim); margin-top:8px; z-index:10;">சமர்ப்பணம் பொத்தானை அழுத்தினால் பலூன் இறைவொளியில் கரைந்துவிடும்!</small>
                    </div>

                    <div class="debrief-box" style="border-color:#10b981; background:rgba(16,185,129,0.08);">
                        <strong style="color:#10b981;">🎯 இறுதிப் போதனை:</strong><br>
                        கைகள் காலியாகும்போது தான் இரு கைகளைக் கூப்பி வணக்கம் செலுத்த முடியும்; பசியுள்ளோருக்கு உணவிட முடியும்; விழுந்தவரைத் தூக்கி விட முடியும்.
                        அனைத்துச் செயல்களையும் செய்யுங்கள்; ஆனால் பலனை ஈஸ்வரனிடம் அர்ப்பணித்து விடுங்கள் — அதுவே <strong>நிஷ்காமிய கர்மா!</strong>
                    </div>
                </div>

                <!-- 5 VALEDICTORY SANKALPAM RESOLUTIONS -->
                <div class="interactive-widget" style="border:2px solid var(--saffron-primary); background:rgba(245,158,11,0.05); margin-top:28px;">
                    <h3 style="font-family:var(--font-heading); color:var(--saffron-primary); text-align:center; font-size:1.5rem; margin-bottom:12px;">
                        📜 5 மணி நேரப் பயிற்சிப் பட்டறை நிறைவுச் சங்கல்பம் (Valedictory Resolutions)
                    </h3>
                    <p style="text-align:center; color:var(--text-muted); font-size:0.95rem; margin-bottom:20px;">
                        இன்று முதல் எனது அன்றாட வாழ்க்கையில் கடைப்பிடிக்க நான் ஏற்கும் 5 புனித உறுதிமொழிகள்:
                    </p>

                    <div class="card-grid-2">
                        <div class="base-card">
                            <h4 style="color:#10b981; margin-bottom:4px;">1. நித்ய விழிப்பு &amp; நன்றி</h4>
                            <p style="font-size:0.85rem; color:var(--text-muted);">காலையில் எழுந்ததும் என் கைகளைக் கண்டு இறைவனுக்கு நன்றி கூறுவேன்; 1 நிமிடம் அமைதி காப்பேன்.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#3b82f6; margin-bottom:4px;">2. பெற்றோர் வழிபாடு (பித்ரு கடன்)</h4>
                            <p style="font-size:0.85rem; color:var(--text-muted);">முதுமையில் உள்ள என் பெற்றோரையும் பெரியோர்களையும் இன்முகத்தோடு பணிவிடை செய்வேன்.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#f59e0b; margin-bottom:4px;">3. இயற்கைக் கொடை (பூத யக்ஞம்)</h4>
                            <p style="font-size:0.85rem; color:var(--text-muted);">ஒரு சொட்டு நீரை வீணாக்க மாட்டேன்; வாயில்லாப் பிராணிகளுக்கும் பறவைகளுக்கும் உணவளிப்பேன்.</p>
                        </div>
                        <div class="base-card">
                            <h4 style="color:#8b5cf6; margin-bottom:4px;">4. நிஷ்காமியச் சேவை &amp; பணிவு</h4>
                            <p style="font-size:0.85rem; color:var(--text-muted);">'நான்', 'எனது' என்ற அகந்தையைத் துறந்து, செய்யும் தொழிலை இறைப்பணியாகச் செய்வேன்.</p>
                        </div>
                    </div>

                    <div style="text-align:center; margin-top:24px;">
                        <button class="btn-nav btn-nav-primary" onclick="alert('உங்கள் சங்கல்பம் பதிவானது! வாழ்க சனாதன தர்மம்! வெல்க பாரதம்!')" style="font-size:1rem; padding:12px 28px;">
                            <i data-lucide="check-circle"></i> நான் இந்த 5 சங்கல்பங்களை ஏற்கிறேன்
                        </button>
                    </div>
                </div>

            </section>

        </div>
    </main>

    <!-- Page Footer -->
    <footer class="page-footer">
        <div class="container">
            <p style="font-family:var(--font-heading); font-size:1.1rem; color:var(--text-main); margin-bottom:8px;">
                அறம் — ஷட் கருமங்கள் பயிற்சிப் பட்டறை வழிகாட்டி
            </p>
            <p style="margin-bottom:12px;">
                ஸ்ரீ பாலசுந்தரம் அவர்களின் அருளுரை &amp; சனாதன தர்ம சாஸ்திரங்களின் அடிப்படையில் வடிவமைக்கப்பட்டது.
            </p>
            <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
                <a href="index.html">← முகப்பு (Home Page)</a>
                <a href="#hero">↑ பக்கத்தின் உச்சிக்குச் செல்க</a>
                <a href="https://github.com/karmayogabg/Aram-Karma-" target="_blank" rel="noopener">GitHub Repository</a>
            </div>
            <p style="margin-top:16px; font-size:0.8rem; color:var(--text-dim);">
                © சனாதன தர்ம ஷட் கருமங்கள் வழிகாட்டி திட்டம் • அனைத்து உரிமைகளும் உலக நன்மைக் சமர்ப்பணம்.
            </p>
        </div>
    </footer>

    <!-- Embedded Complete 200 Rishis Data & Interactive Scripts -->
    <script>
        const RISHIS_DATA = {rishis_json_str};

        // Initialize Lucide Icons
        document.addEventListener('DOMContentLoaded', () => {{
            lucide.createIcons();
            initRiceChain();
            initKarmaMatrix();
            renderRishis(RISHIS_DATA);
            initNaraChain();
        }});

        // 1. Bright / Dark Theme Toggle
        function toggleTheme() {{
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            localStorage.setItem('aram_theme', isLight ? 'light' : 'dark');
            updateThemeButton(isLight);
        }}

        function updateThemeButton(isLight) {{
            const label = document.getElementById('theme-label');
            const icon = document.getElementById('theme-icon');
            if (label) label.innerText = isLight ? 'Dark Theme' : 'Bright Theme';
            if (icon) icon.setAttribute('data-lucide', isLight ? 'moon' : 'sun');
            lucide.createIcons();
        }}

        if (localStorage.getItem('aram_theme') === 'light') {{
            document.body.classList.add('light-theme');
            updateThemeButton(true);
        }}

        // 2. Master Session 5-Hour Timer (Play / Pause / Reset)
        let sessionSeconds = 5 * 3600; // 300 minutes
        let sessionTimerInterval = null;
        let isSessionRunning = false;

        function toggleSessionTimer() {{
            const btnText = document.getElementById('timer-btn-text');
            const btnIcon = document.getElementById('timer-btn-icon');
            if (isSessionRunning) {{
                clearInterval(sessionTimerInterval);
                isSessionRunning = false;
                btnText.innerText = 'டைமர் தொடங்கு';
                btnIcon.setAttribute('data-lucide', 'play');
            }} else {{
                isSessionRunning = true;
                btnText.innerText = 'இடைநிறுத்து (Pause)';
                btnIcon.setAttribute('data-lucide', 'pause');
                sessionTimerInterval = setInterval(() => {{
                    if (sessionSeconds > 0) {{
                        sessionSeconds--;
                        updateSessionClock();
                    }} else {{
                        clearInterval(sessionTimerInterval);
                        isSessionRunning = false;
                        playTempleBellSound();
                        alert('5 மணி நேர பயிற்சிப் பட்டறை அமர்வு வெற்றிகரமாக நிறைவு பெற்றது!');
                    }}
                }}, 1000);
            }}
            lucide.createIcons();
        }}

        function resetSessionTimer() {{
            clearInterval(sessionTimerInterval);
            isSessionRunning = false;
            sessionSeconds = 5 * 3600;
            updateSessionClock();
            document.getElementById('timer-btn-text').innerText = 'டைமர் தொடங்கு';
            document.getElementById('timer-btn-icon').setAttribute('data-lucide', 'play');
            lucide.createIcons();
        }}

        function updateSessionClock() {{
            const h = Math.floor(sessionSeconds / 3600);
            const m = Math.floor((sessionSeconds % 3600) / 60);
            const s = sessionSeconds % 60;
            document.getElementById('session-clock').innerText = 
                `${{String(h).padStart(2, '0')}}:${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;
        }}

        // 3. Audio Synthesizer (Temple Bell Gong using Web Audio API)
        function playTempleBellSound() {{
            try {{
                const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                const now = audioCtx.currentTime;
                
                // Fundamental + harmonics for rich bronze temple bell chime
                const freqs = [432, 864, 1296, 1728];
                freqs.forEach((freq, idx) => {{
                    const osc = audioCtx.createOscillator();
                    const gain = audioCtx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(freq, now);
                    
                    gain.gain.setValueAtTime(0.3 / (idx + 1), now);
                    gain.gain.exponentialRampToValueAtTime(0.0001, now + 3.5);
                    
                    osc.connect(gain);
                    gain.connect(audioCtx.destination);
                    osc.start(now);
                    osc.stop(now + 3.6);
                }});
            }} catch (e) {{
                console.log('AudioContext not allowed without gesture', e);
            }}
        }}

        // 4. 1-Minute Padmasana Meditation Timer
        let medSeconds = 60;
        let medInterval = null;

        function startMeditationTimer() {{
            if (medInterval) clearInterval(medInterval);
            medSeconds = 60;
            document.getElementById('btn-med-timer').disabled = true;
            playTempleBellSound();

            medInterval = setInterval(() => {{
                medSeconds--;
                const m = Math.floor(medSeconds / 60);
                const s = medSeconds % 60;
                document.getElementById('meditation-timer-display').innerText = 
                    `${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;
                
                if (medSeconds <= 0) {{
                    clearInterval(medInterval);
                    document.getElementById('btn-med-timer').disabled = false;
                    playTempleBellSound();
                    setTimeout(() => {{
                        alert('1 நிமிட மௌனம் நிறைவு பெற்றது! உங்கள் அனுபவத்தைப் பகிருங்கள்.');
                    }}, 200);
                }}
            }}, 1000);
        }}

        function resetMeditationTimer() {{
            if (medInterval) clearInterval(medInterval);
            medSeconds = 60;
            document.getElementById('meditation-timer-display').innerText = '01:00';
            document.getElementById('btn-med-timer').disabled = false;
        }}

        // 5. Rice Dependency Chain Simulator
        const RICE_NODES = [
            '1. பூமித் தாய் & வண்டல் மண்', '2. சூரிய பகவான் (வெப்பம்)', '3. வருண பகவான் (மழை/நீர்)',
            '4. நிலத்து மண்புழுக்கள்', '5. நிலத்தை உழுத காளை/பசு', '6. வியர்வை சிந்திய உழவர்',
            '7. கால்வாய் பாசனப் பொறியாளர்', '8. அறுவடை & நெற்கதிர் பிரிப்பாளர்', '9. சணல் சாக்கு நெய்தவர்',
            '10. 500 கிமீ ஏற்றிவந்த லாரி ஓட்டுநர்', '11. மொத்த விற்பனை மண்டி', '12. சில்லறை மளிகைக் கடை',
            '13. இரும்பு பாத்திரம் செய்த கொல்லர்', '14. தூத்துக்குடி உப்பு காய்ச்சியவர்', '15. சமையல் எரிவாயு சிலிண்டர்',
            '16. அன்பு கூர்ந்து சமைத்தவர்'
        ];
        let brokenNodes = new Set();

        function initRiceChain() {{
            const c = document.getElementById('rice-chain-container');
            if (!c) return;
            c.innerHTML = '';
            RICE_NODES.forEach((name, idx) => {{
                const div = document.createElement('div');
                div.className = 'rice-chain-node';
                div.id = `rice-node-${{idx}}`;
                div.innerHTML = `<i data-lucide="link"></i> <span>${{name}}</span>`;
                div.onclick = () => toggleRiceNode(idx);
                c.appendChild(div);
            }});
            lucide.createIcons();
        }}

        function toggleRiceNode(idx) {{
            const node = document.getElementById(`rice-node-${{idx}}`);
            if (brokenNodes.has(idx)) {{
                brokenNodes.delete(idx);
                node.classList.remove('broken');
            }} else {{
                brokenNodes.add(idx);
                node.classList.add('broken');
            }}
            updateRiceStatus();
        }}

        function resetRiceChain() {{
            brokenNodes.clear();
            document.querySelectorAll('.rice-chain-node').forEach(n => n.classList.remove('broken'));
            updateRiceStatus();
        }}

        function updateRiceStatus() {{
            const s = document.getElementById('rice-chain-status');
            if (brokenNodes.size > 0) {{
                s.style.background = 'rgba(239, 68, 68, 0.15)';
                s.style.color = '#ef4444';
                s.innerHTML = `❌ <strong>சங்கிலி முறிந்தது (${{brokenNodes.size}} இணைப்புகள் துண்டிக்கப்பட்டன)!</strong> ஒரு பிடி சோறு உங்கள் தட்டை வந்து சேர முடியாது! பசியில் வாட நேரிடும். எனவே 'நான்' என்ற எண்ணம் தவறு!`;
            }} else {{
                s.style.background = 'rgba(16, 185, 129, 0.12)';
                s.style.color = '#10b981';
                s.innerHTML = `✅ அனைத்து 16 சங்கிலிகளும் இணைந்து இயங்குகின்றன — ஒரு பிடி சோறு உங்கள் தட்டிற்கு வெற்றிகரமாக வந்து சேர்கிறது!`;
            }}
        }}

        // 6. Interactive 12-Scenario Karma Classification Matrix
        const SCENARIOS = [
            {{ q: "காலையில் எழுந்து பல் துலக்கி, நீராடி சூரிய நமஸ்காரம் செய்தல்", ans: "nitya", exp: "தினந்தோறும் செய்ய வேண்டிய உடல்தூய்மை & நித்ய கடமை." }},
            {{ q: "அமாவாசை தோறும் மறைந்த முன்னோர்களுக்கு எள், தண்ணீர் இறைத்து தர்ப்பணம் செய்தல்", ans: "naimittika", exp: "அமாவாசை எனும் கால நிகழ்வை முன்னிட்டுச் செய்யும் கடமை." }},
            {{ q: "புதிய வியாபாரத்தில் கோடிக்கணக்கில் லாபம் ஈட்ட வேண்டும் என்று சிறப்பு யாகம் நடத்துதல்", ans: "kamya", exp: "சுய லாப ஆசையை முன்னிறுத்திச் செய்யப்படும் காம்ய கர்மா." }},
            {{ q: "விபத்தில் காயமடைந்த ஒருவருக்கு பெயர் கூடச் சொல்லாமல் முதலுதவி செய்து காப்பாற்றுதல்", ans: "nishkamya", exp: "எந்தப் பலனும் பாராது இறை அர்ப்பணமாகச் செய்யும் தூய சேவை." }},
            {{ q: "கோபத்தில் ஒருவரைத் தவறாகப் பேசிவிட்டதால் மனம் வருந்தி மன்னிப்புக் கேட்டு 1 நாள் விரதம் இருத்தல்", ans: "prayaschitta", exp: "செய்த குற்றத்திற்கு வருந்தி மனச்சுத்தி தேடும் பிராயச்சித்தம்." }},
            {{ q: "அரசு அலுவலகத்தில் காரியம் நடக்க லஞ்சம் கொடுத்தல் அல்லது பிறர் நிலத்தை அபகரித்தல்", ans: "nishiddha", exp: "சாஸ்திரத்தாலும் நீதியாலும் முற்றிலும் தடைசெய்யப்பட்ட கொடும் பாவம்." }},
            {{ q: "வீட்டில் தினமும் சமையல் செய்த பின் காக்கை மற்றும் எறும்புகளுக்கு உணவிடுதல்", ans: "nitya", exp: "நித்ய பஞ்ச மகா யக்ஞத்தில் பூத யக்ஞக் கடமை." }},
            {{ q: "சூரிய கிரகணம் அல்லது சந்திர கிரகணத்தின் போது நதியில் நீராடி தியானித்தல்", ans: "naimittika", exp: "கிரகணம் எனும் வானியல் கால நிகழ்வுக் கடமை." }},
            {{ q: "பரீட்சையில் முதல் ரேங்க் வர வேண்டும் என்பதற்காக 108 தேங்காய் உடைத்து வேண்டுதல்", ans: "kamya", exp: "சுய வெற்றிப் பலனை எதிர்பார்த்துச் செய்யப்படும் காம்யம்." }},
            {{ q: "தெருவோரக் குழந்தைகளுக்கும் முதியோருக்கும் புகழின்றி அமைதியாக உணவளித்தல்", ans: "nishkamya", exp: "ஈஸ்வர சமர்ப்பண லோக க்ஷேம சேவை." }},
            {{ q: "தெரியாமல் மரக்கிளையை முறித்துவிட்டதற்காக 5 புதிய மரக்கன்றுகளை நட்டு வளர்த்தல்", ans: "prayaschitta", exp: "பூத துரோகத்திற்கான பசுமைப் பிராயச்சித்தம்." }},
            {{ q: "பொய் சாட்சி கூறி ஒரு அப்பாவிக்குச் சிறை தண்டனை பெற்றுத் தருதல்", ans: "nishiddha", exp: "வள்ளலார் எச்சரிக்கும் 44 மாபாவங்களில் ஒன்று." }}
        ];
        let userKarmaScore = 0;
        let answeredScenarios = new Set();

        function initKarmaMatrix() {{
            const c = document.getElementById('karma-scenario-list');
            if (!c) return;
            c.innerHTML = '';
            userKarmaScore = 0;
            answeredScenarios.clear();
            document.getElementById('matrix-score').innerText = '0';

            SCENARIOS.forEach((item, idx) => {{
                const div = document.createElement('div');
                div.className = 'base-card';
                div.id = `scenario-card-${{idx}}`;
                div.innerHTML = `
                    <div style="font-weight:700; font-size:0.9rem; margin-bottom:10px;">${{idx + 1}}. ${{item.q}}</div>
                    <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:8px;">
                        <button class="btn-timer" onclick="submitKarmaAnswer(${{idx}}, 'nitya')">நித்யம்</button>
                        <button class="btn-timer" onclick="submitKarmaAnswer(${{idx}}, 'naimittika')">நைமித்திகம்</button>
                        <button class="btn-timer" onclick="submitKarmaAnswer(${{idx}}, 'kamya')">காம்யம்</button>
                        <button class="btn-timer" onclick="submitKarmaAnswer(${{idx}}, 'nishkamya')">நிஷ்காம்யம்</button>
                        <button class="btn-timer" onclick="submitKarmaAnswer(${{idx}}, 'prayaschitta')">பிராயச்சித்தம்</button>
                        <button class="btn-timer" onclick="submitKarmaAnswer(${{idx}}, 'nishiddha')">நிஷித்தம்</button>
                    </div>
                    <div id="scenario-feedback-${{idx}}" style="font-size:0.8rem; display:none; padding:6px; border-radius:4px;"></div>
                `;
                c.appendChild(div);
            }});
        }}

        function submitKarmaAnswer(idx, chosen) {{
            if (answeredScenarios.has(idx)) return;
            answeredScenarios.add(idx);

            const item = SCENARIOS[idx];
            const fb = document.getElementById(`scenario-feedback-${{idx}}`);
            fb.style.display = 'block';

            if (chosen === item.ans) {{
                userKarmaScore++;
                fb.style.background = 'rgba(16,185,129,0.15)';
                fb.style.color = '#10b981';
                fb.innerHTML = `✅ <strong>மிகச் சரி!</strong> ${{item.exp}}`;
            }} else {{
                fb.style.background = 'rgba(239,68,68,0.15)';
                fb.style.color = '#ef4444';
                fb.innerHTML = `❌ <strong>தவறு!</strong> சரியான விடை: <strong>${{item.ans.toUpperCase()}}</strong> — ${{item.exp}}`;
            }}
            document.getElementById('matrix-score').innerText = userKarmaScore;
        }}

        function resetKarmaMatrix() {{
            initKarmaMatrix();
        }}

        // 7. Pitru Yagnam Star Board
        let starCounts = [0, 1, 3, 6, 0];
        let totalStarsAvailable = 10;

        function changeStar(colIdx, delta) {{
            const currentTotal = starCounts.reduce((a, b) => a + b, 0);
            if (delta > 0 && currentTotal >= 10) {{
                alert('அனைத்து 10 நட்சத்திரங்களும் பயன்படுத்தப்பட்டுவிட்டன! வேறு கட்டத்திலிருந்து குறைத்து மாற்றவும்.');
                return;
            }}
            if (delta < 0 && starCounts[colIdx] <= 0) return;

            starCounts[colIdx] += delta;
            document.getElementById(`star-count-${{colIdx}}`).innerText = `⭐ ${{starCounts[colIdx]}}`;
            
            const newTotal = starCounts.reduce((a, b) => a + b, 0);
            document.getElementById('stars-remaining').innerText = 10 - newTotal;
        }}

        // 8. Live Nara Yagnam Debate Logger
        const DEFAULT_NARA = [
            {{ role: "ஆசிரியர் (Teacher)", help: "ஞானம், கல்வி மற்றும் ஒழுக்கம் புகட்டுகிறார்" }},
            {{ role: "துப்புரவுப் பணியாளர் (Sanitation)", help: "குப்பைகளை அகற்றி தொற்றுநோய் வராமல் ஊரைக் காக்கிறார்" }},
            {{ role: "விவசாயி (Farmer)", help: "சேற்றில் கால் வைத்து சோறு தந்து உயிர் வளர்க்கிறார்" }},
            {{ role: "பேருந்து ஓட்டுநர் (Bus Driver)", help: "மழை, வெயில் பாராது மக்களைச் சேருமிடத்தில் சேர்க்கிறார்" }},
            {{ role: "தையல்காரர் (Tailor)", help: "மானத்தைக் காக்க உடைகளைத் தைத்துத் தருகிறார்" }},
            {{ role: "ராணுவ வீரர் (Soldier)", help: "எல்லையில் பனியில் கண்விழித்து நம் நிம்மதியைக் காக்கிறார்" }}
        ];

        function initNaraChain() {{
            const c = document.getElementById('nara-chain-list');
            if (!c) return;
            c.innerHTML = '';
            DEFAULT_NARA.forEach((item, idx) => {{
                const d = document.createElement('div');
                d.className = 'base-card';
                d.style.padding = '10px 14px';
                d.innerHTML = `<strong>${{idx + 1}}. ${{item.role}}</strong>: <span style="color:var(--text-muted); font-size:0.85rem;">${{item.help}}</span>`;
                c.appendChild(d);
            }});
        }}

        function addNaraChainItem() {{
            const role = prompt('மனிதரின் பணி/தொழில் என்ன? (எ.கா: மின்வாரிய ஊழியர்)');
            if (!role) return;
            const help = prompt('அவர் சமுதாயத்திற்கு என்ன உதவி செய்கிறார்? (எ.கா: புயலிலும் மின்சாரம் மீட்டெடுக்கிறார்)');
            if (!help) return;
            DEFAULT_NARA.push({{ role, help }});
            initNaraChain();
        }}

        function resetNaraChain() {{
            initNaraChain();
        }}

        // 9. 200 Rishis Search and Categorization Engine
        let currentRishiCat = 'all';

        function renderRishis(list) {{
            const c = document.getElementById('rishi-list-container');
            if (!c) return;
            c.innerHTML = '';
            list.forEach(r => {{
                const card = document.createElement('div');
                card.className = 'rishi-item-card';
                card.innerHTML = `
                    <div class="rishi-top-row">
                        <span class="rishi-num">#${{r.id}}</span>
                        <span class="rishi-category-tag">${{r.category_ta}}</span>
                    </div>
                    <div class="rishi-names">
                        ${{r.name_ta}} <small>(${{r.name_en}})</small>
                    </div>
                    <p class="rishi-desc">${{r.contrib_ta}}</p>
                    <small style="color:var(--text-dim); font-size:0.75rem;">${{r.contrib_en}}</small>
                `;
                c.appendChild(card);
            }});
            document.getElementById('rishi-counter-text').innerText = `காண்கிறது: ${{list.length}} / 200 ரிஷிகள்`;
        }}

        function filterRishis() {{
            const query = (document.getElementById('rishi-search-box').value || '').toLowerCase().trim();
            const filtered = RISHIS_DATA.filter(r => {{
                const matchCat = (currentRishiCat === 'all') ||
                    (currentRishiCat === 'saptarishi' && (r.category_ta.includes('சப்தரிஷி') || r.category_ta.includes('பிரஜாபதி'))) ||
                    (currentRishiCat === 'vedic' && r.category_ta.includes('வேத')) ||
                    (currentRishiCat === 'rishika' && (r.category_ta.includes('ரிஷிகை') || r.category_ta.includes('பிரம்மவாதினி') || r.category_ta.includes('பெண்'))) ||
                    (currentRishiCat === 'upanishad' && r.category_ta.includes('உபநிடத')) ||
                    (currentRishiCat === 'siddha' && (r.category_ta.includes('சித்தர்') || r.category_ta.includes('நாயன்மார்') || r.category_ta.includes('முனிவர்') && r.id >= 146 && r.id <= 175)) ||
                    (currentRishiCat === 'shastra' && (r.category_ta.includes('சூத்திர') || r.category_ta.includes('சாஸ்திர') || r.category_ta.includes('விஞ்ஞான') || r.category_ta.includes('கணித')));
                
                const matchQuery = !query || 
                    r.name_ta.toLowerCase().includes(query) || 
                    r.name_en.toLowerCase().includes(query) || 
                    r.contrib_ta.toLowerCase().includes(query) || 
                    r.contrib_en.toLowerCase().includes(query) ||
                    r.category_ta.toLowerCase().includes(query);

                return matchCat && matchQuery;
            }});
            renderRishis(filtered);
        }}

        function setRishiCategory(cat, btn) {{
            currentRishiCat = cat;
            document.querySelectorAll('#rishi-cat-pills button').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            filterRishis();
        }}

        function randomPickTwoRishis() {{
            const r1 = RISHIS_DATA[Math.floor(Math.random() * RISHIS_DATA.length)];
            let r2 = RISHIS_DATA[Math.floor(Math.random() * RISHIS_DATA.length)];
            while (r2.id === r1.id) {{
                r2 = RISHIS_DATA[Math.floor(Math.random() * RISHIS_DATA.length)];
            }}
            const disp = document.getElementById('picked-rishis-display');
            disp.style.display = 'block';
            disp.innerHTML = `
                <h4 style="color:#8b5cf6; margin-bottom:8px;">✨ உங்கள் வாழ்விற்கான 2 வழிகாட்டி ரிஷிகள் தேர்ந்தெடுக்கப்பட்டனர்:</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                    <div style="background:var(--bg-card); padding:10px; border-radius:6px;">
                        <strong style="color:var(--saffron-primary);">1. ${{r1.name_ta}} (${{r1.name_en}})</strong>
                        <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">${{r1.contrib_ta}}</p>
                    </div>
                    <div style="background:var(--bg-card); padding:10px; border-radius:6px;">
                        <strong style="color:var(--saffron-primary);">2. ${{r2.name_ta}} (${{r2.name_en}})</strong>
                        <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">${{r2.contrib_ta}}</p>
                    </div>
                </div>
                <p style="font-size:0.8rem; color:var(--text-main); margin-top:8px; font-weight:700;">
                    🎯 சங்கல்பம்: இந்த இரு ரிஷிகளின் நூல்களையோ அல்லது சரிதத்தையோ இந்த வருடம் படித்து வாழ்க்கையில் கடைப்பிடிப்பேன்!
                </p>
            `;
        }}

        // 10. Cosmic Zoom Out Slider
        const COSMIC_LEVELS = [
            {{ title: "நிலை 1: இந்தப் பயிற்சி அரங்கம் (This Workshop Hall)", icon: "🏛️", desc: "நாம் தற்போது அமர்ந்திருக்கும் சில நூறு சதுர அடி அறை. இங்கு அமர்ந்து கொண்டு நாம் நம்மைப் பேரறிவாளியாக நினைக்கிறோம்." }},
            {{ title: "நிலை 2: நமது கிராமம் / நகரம் (Village / Town)", icon: "🏡", desc: "நமது ஊரில் லட்சக்கணக்கான மக்கள் வாழ்கிறார்கள். அவர்களில் நாம் ஒரு சிறிய குடும்பம் மட்டுமே." }},
            {{ title: "நிலை 3: நமது மாவட்டம் & தமிழ்நாடு (Tamil Nadu)", icon: "🌾", desc: "8 கோடி தமிழர்கள் வாழும் நிலப்பரப்பு. இதில் நமது அடையாளம் ஒரு சிறு முகவரி மட்டுமே." }},
            {{ title: "நிலை 4: பாரத தேசம் (Bharata Varsha)", icon: "🇮🇳", desc: "140 கோடி மனிதர்கள், இமயமலை முதல் குமரி வரை விரிந்த புண்ணிய பூமி." }},
            {{ title: "நிலை 5: பூமிப் பந்து (Planet Earth)", icon: "🌍", desc: "800 கோடி மனிதர்கள், 10 மில்லியன் வகை உயிரினங்கள் வாழும் நீலக் கிரகம்." }},
            {{ title: "நிலை 6: சூரியக் குடும்பம் (Solar System)", icon: "☀️", desc: "பூமியைப் போல 13 லட்சம் பூமிகளைத் தனக்குள் அடக்கக்கூடிய சூரியனைச் சுற்றிச் சுழலும் சிறு கோள் நமது பூமி!" }},
            {{ title: "நிலை 7: பால்வெளி அண்டம் (Milky Way Galaxy)", icon: "🌀", desc: "நமது சூரியனைப் போல 10,000 கோடி (100 Billion) நட்சத்திரங்கள் அடங்கிய சுழல் விண்மீன் மண்டலம்!" }},
            {{ title: "நிலை 8: காணக்கூடிய பேரண்டம் (Observable Universe)", icon: "🌌", desc: "பால்வெளியைப் போல 2 லட்சம் கோடி (2 Trillion) விண்மீன் மண்டலங்கள்! இதில் மனிதன் என்பவன் ஒரு தூசிலும் தூசு! எதற்கு வீண் அகந்தை?" }}
        ];

        function updateCosmicScale(val) {{
            const idx = parseInt(val, 10) - 1;
            const item = COSMIC_LEVELS[idx];
            document.getElementById('cosmic-title').innerText = item.title;
            document.getElementById('cosmic-icon').innerText = item.icon;
            document.getElementById('cosmic-desc').innerText = item.desc;
        }}

        // 11. Nishkamya Balloon Release Simulator
        function releaseBalloon() {{
            const input = document.getElementById('ego-input');
            const balloon = document.getElementById('interactive-balloon');
            const balloonText = document.getElementById('balloon-text');
            const val = input.value.trim() || 'அகந்தை & எதிர்பார்ப்பு';
            
            balloonText.innerText = val;
            playTempleBellSound();
            balloon.classList.add('released');

            setTimeout(() => {{
                alert(`✨ அற்புதம்! '${{val}}' ஈஸ்வரனிடம் சமர்ப்பிக்கப்பட்டது! உங்கள் கைகளும் மனதும் பந்தங்களிலிருந்து விடுபட்டன!`);
                balloon.classList.remove('released');
                balloonText.innerText = 'நான் & எனது';
                input.value = '';
            }}, 2000);
        }}

        // 12. Active Agenda Link on Scroll
        window.addEventListener('scroll', () => {{
            const hours = [1, 2, 3, 4, 5];
            const scrollPos = window.scrollY + 140;
            hours.forEach(h => {{
                const sec = document.getElementById(`hour-${{h}}`);
                const link = document.getElementById(`agenda-link-${{h}}`);
                if (sec && link) {{
                    const top = sec.offsetTop;
                    const height = sec.offsetHeight;
                    if (scrollPos >= top && scrollPos < top + height) {{
                        link.classList.add('active');
                    }} else {{
                        link.classList.remove('active');
                    }}
                }}
            }});
        }});
    </script>
</body>
</html>
"""

    with open('AgendaAndTeaching.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    os.makedirs('AgendaAndTeaching', exist_ok=True)
    with open('AgendaAndTeaching/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated AgendaAndTeaching.html ({len(html_content)} bytes)")
    print("Generated AgendaAndTeaching/index.html successfully!")

if __name__ == '__main__':
    main()
