# -*- coding: utf-8 -*-
import os
import shutil

html_path = "/home/sabrisatharamanathan/my-project/Aram-Karma/Karma-WorkshopActivities.html"
index_path = "/home/sabrisatharamanathan/my-project/Aram-Karma/index.html"

print("Compiling Karma Workshop Activities HTML...")

# Part 1: HTML Head and CSS
head_and_css = """<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ஷட் கருமங்கள் பயிற்சிப் பட்டறை வழிகாட்டி — 5 மணி நேர முழுமையான செயல்முறைக் கையேடு</title>
    <meta name="description" content="ஸ்ரீ பாலசுந்தரம் அவர்களின் சனாதன தர்ம ஷட் கருமங்கள்: நித்ய, நைமித்திக, காம்ய, நிஷ்காம்ய, பிராயச்சித்த, நிஷித்த கர்மாக்களின் 5 மணி நேர விரிவான பயிற்சிப் பட்டறை வழிகாட்டி, குழுச் செயல்பாடுகள் மற்றும் சுலோகப் பேழை.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Mukta+Malar:wght@400;500;600;700;800&family=Noto+Sans+Tamil:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        :root {
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
            --karma-nitya-bg: rgba(16, 185, 129, 0.1);
            --karma-naimittika: #3b82f6;
            --karma-naimittika-bg: rgba(59, 130, 246, 0.1);
            --karma-kamya: #f59e0b;
            --karma-kamya-bg: rgba(245, 158, 11, 0.1);
            --karma-nishkamya: #8b5cf6;
            --karma-nishkamya-bg: rgba(139, 92, 246, 0.1);
            --karma-prayaschitta: #06b6d4;
            --karma-prayaschitta-bg: rgba(6, 182, 212, 0.1);
            --karma-nishiddha: #ef4444;
            --karma-nishiddha-bg: rgba(239, 68, 68, 0.1);
            
            --font-heading: 'Outfit', 'Cinzel', 'Noto Sans Tamil', sans-serif;
            --font-tamil: 'Noto Sans Tamil', 'Mukta Malar', sans-serif;
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --shadow-md: 0 10px 30px rgba(0,0,0,0.4);
            --shadow-lg: 0 16px 40px rgba(0,0,0,0.6);
        }

        /* Bright / Light Theme */
        body.light-theme {
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
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: var(--font-tamil);
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.75;
            -webkit-font-smoothing: antialiased;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .container {
            max-width: 1320px;
            margin: 0 auto;
            padding: 0 24px;
        }

        /* Navbar */
        .navbar {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(15, 20, 31, 0.92);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-color);
            padding: 12px 0;
            transition: all 0.3s ease;
        }
        body.light-theme .navbar {
            background: rgba(255, 255, 255, 0.95);
        }
        .navbar-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--text-main);
        }
        .brand-logo {
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
        }
        .brand-text h1 {
            font-family: var(--font-heading);
            font-size: 1.15rem;
            font-weight: 800;
            line-height: 1.25;
            color: var(--text-main);
        }
        .brand-text p {
            font-size: 0.78rem;
            color: var(--saffron-primary);
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        .btn-nav {
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
        }
        .btn-nav:hover {
            border-color: var(--saffron-primary);
            color: var(--saffron-primary);
            transform: translateY(-1px);
        }
        .btn-nav-primary {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #000;
            border-color: var(--saffron-primary);
            font-weight: 800;
        }
        .btn-nav-primary:hover {
            background: #d97706;
            color: #000;
            box-shadow: 0 4px 14px var(--saffron-glow);
        }

        /* Hero Banner */
        .hero {
            padding: 50px 0 36px 0;
            text-align: center;
            background: radial-gradient(circle at 50% 15%, rgba(245, 158, 11, 0.16), transparent 70%);
            border-bottom: 1px solid var(--border-color);
            position: relative;
        }
        .hero-badge-wrap {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }
        .hero-badge {
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
        }
        .hero-title {
            font-family: var(--font-heading);
            font-size: clamp(1.8rem, 4vw, 2.7rem);
            font-weight: 900;
            line-height: 1.3;
            margin-bottom: 14px;
            color: var(--text-main);
            letter-spacing: -0.5px;
        }
        .hero-title span {
            background: linear-gradient(135deg, #f59e0b, #fbbf24, #f97316);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-quote {
            max-width: 860px;
            margin: 0 auto 20px auto;
            font-size: 1.05rem;
            color: var(--text-muted);
            line-height: 1.8;
            font-style: italic;
            border-left: 3px solid var(--saffron-primary);
            padding: 10px 20px;
            background: rgba(245, 158, 11, 0.05);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            text-align: left;
        }
        .quick-stats-bar {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 24px;
        }
        .stat-chip {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            padding: 10px 18px;
            border-radius: var(--radius-md);
            font-size: 0.88rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: all 0.2s ease;
        }
        .stat-chip:hover {
            border-color: var(--saffron-primary);
            transform: translateY(-2px);
        }

        /* Navigation Anchor Bar */
        .section-anchor-bar {
            position: sticky;
            top: 73px;
            z-index: 900;
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-color);
            padding: 10px 0;
            display: flex;
            gap: 10px;
            overflow-x: auto;
            white-space: nowrap;
            box-shadow: 0 4px 16px rgba(0,0,0,0.25);
        }
        .anchor-pill {
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 999px;
            font-weight: 700;
            font-size: 0.86rem;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            transition: all 0.2s ease;
        }
        .anchor-pill:hover, .anchor-pill.active {
            border-color: var(--saffron-primary);
            background: var(--saffron-glow);
            color: var(--saffron-primary);
            transform: translateY(-1px);
        }

        /* Main Content Layout */
        .main-layout {
            padding: 44px 0 90px 0;
        }
        .section-block {
            margin-bottom: 64px;
            scroll-margin-top: 130px;
        }
        .section-header-title {
            font-family: var(--font-heading);
            font-size: 1.85rem;
            font-weight: 900;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-main);
        }
        .section-header-subtitle {
            font-size: 1rem;
            color: var(--text-muted);
            margin-bottom: 26px;
            max-width: 950px;
            line-height: 1.7;
        }

        /* 5-Hour Session Roadmap Timeline */
        .timeline-track {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
            margin: 24px 0 32px 0;
        }
        .timeline-hour-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 20px;
            position: relative;
            transition: all 0.25s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .timeline-hour-card:hover {
            border-color: var(--saffron-primary);
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }
        .hour-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.76rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
            width: fit-content;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        .hour-1-b { background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.35); }
        .hour-2-b { background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.35); }
        .hour-3-b { background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.35); }
        .hour-4-b { background: rgba(139, 92, 246, 0.15); color: #8b5cf6; border: 1px solid rgba(139, 92, 246, 0.35); }
        .hour-5-b { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.35); }

        .hour-time {
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--text-dim);
            margin-bottom: 4px;
        }
        .hour-title {
            font-family: var(--font-heading);
            font-size: 1.15rem;
            font-weight: 800;
            margin-bottom: 8px;
            color: var(--text-main);
            line-height: 1.35;
        }
        .hour-desc {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 12px;
        }
        .hour-activity-chip {
            background: var(--bg-card);
            border: 1px dashed var(--border-color);
            padding: 8px 12px;
            border-radius: var(--radius-sm);
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--saffron-primary);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Karma 3-Ties Matrix (Sanchita, Prarabdha, Agami) */
        .karma-ties-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin: 24px 0;
        }
        .tie-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 24px;
            position: relative;
            box-shadow: var(--shadow-md);
            transition: all 0.25s ease;
        }
        .tie-card:hover {
            transform: translateY(-3px);
            border-color: var(--saffron-primary);
        }
        .tie-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }
        .tie-badge {
            font-size: 0.75rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
            text-transform: uppercase;
        }
        .tie-title {
            font-family: var(--font-heading);
            font-size: 1.3rem;
            font-weight: 800;
            margin-bottom: 8px;
            color: var(--text-main);
        }
        .tie-metaphor {
            font-size: 0.92rem;
            color: var(--saffron-primary);
            font-weight: 700;
            margin-bottom: 12px;
        }
        .tie-body {
            font-size: 0.92rem;
            color: var(--text-muted);
            line-height: 1.7;
        }

        /* 6 Karma Overview Cards */
        .karma-six-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 24px;
            margin: 28px 0;
        }
        .karma-card {
            background: var(--bg-surface);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 28px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            transition: all 0.25s ease;
            box-shadow: var(--shadow-md);
        }
        .karma-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        .karma-card.card-nitya:hover { border-color: var(--karma-nitya); }
        .karma-card.card-naimittika:hover { border-color: var(--karma-naimittika); }
        .karma-card.card-kamya:hover { border-color: var(--karma-kamya); }
        .karma-card.card-nishkamya:hover { border-color: var(--karma-nishkamya); }
        .karma-card.card-prayaschitta:hover { border-color: var(--karma-prayaschitta); }
        .karma-card.card-nishiddha:hover { border-color: var(--karma-nishiddha); }

        .karma-tag-strip {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
        }
        .karma-badge {
            font-size: 0.78rem;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 999px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .b-nitya { background: var(--karma-nitya-bg); color: var(--karma-nitya); border: 1px solid rgba(16, 185, 129, 0.3); }
        .b-naimittika { background: var(--karma-naimittika-bg); color: var(--karma-naimittika); border: 1px solid rgba(59, 130, 246, 0.3); }
        .b-kamya { background: var(--karma-kamya-bg); color: var(--karma-kamya); border: 1px solid rgba(245, 158, 11, 0.3); }
        .b-nishkamya { background: var(--karma-nishkamya-bg); color: var(--karma-nishkamya); border: 1px solid rgba(139, 92, 246, 0.3); }
        .b-prayaschitta { background: var(--karma-prayaschitta-bg); color: var(--karma-prayaschitta); border: 1px solid rgba(6, 182, 212, 0.3); }
        .b-nishiddha { background: var(--karma-nishiddha-bg); color: var(--karma-nishiddha); border: 1px solid rgba(239, 68, 68, 0.3); }

        .karma-card h3 {
            font-family: var(--font-heading);
            font-size: 1.45rem;
            font-weight: 800;
            margin-bottom: 6px;
            color: var(--text-main);
        }
        .karma-motto {
            font-size: 0.92rem;
            font-weight: 700;
            color: var(--saffron-primary);
            margin-bottom: 14px;
        }
        .karma-content {
            font-size: 0.94rem;
            color: var(--text-muted);
            line-height: 1.75;
            margin-bottom: 16px;
        }
        .karma-key-points {
            list-style: none;
            margin: 14px 0;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .karma-key-points li {
            font-size: 0.88rem;
            color: var(--text-main);
            display: flex;
            align-items: flex-start;
            gap: 8px;
            line-height: 1.5;
        }
        .karma-key-points li i {
            color: var(--saffron-primary);
            margin-top: 3px;
            flex-shrink: 0;
        }

        /* 16 Shodasha Samskaras Interactive Grid */
        .samskaras-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin: 24px 0;
        }
        .samskara-pill-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 16px 18px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
            transition: all 0.2s ease;
        }
        .samskara-pill-card:hover {
            border-color: #3b82f6;
            background: var(--bg-card);
            transform: translateY(-2px);
        }
        .samskara-num {
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: rgba(59, 130, 246, 0.15);
            color: #3b82f6;
            border: 1px solid rgba(59, 130, 246, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 0.85rem;
            flex-shrink: 0;
        }
        .samskara-details h4 {
            font-size: 1rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 2px;
        }
        .samskara-stage {
            font-size: 0.78rem;
            color: #3b82f6;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .samskara-desc {
            font-size: 0.84rem;
            color: var(--text-muted);
            line-height: 1.5;
        }

        /* 5 Pancha Maha Yagnas Cards */
        .yagnas-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
            margin: 20px 0;
        }
        .yagna-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 20px;
            transition: all 0.2s ease;
        }
        .yagna-card:hover {
            border-color: #10b981;
            transform: translateY(-2px);
        }
        .yagna-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }
        .yagna-icon {
            width: 36px;
            height: 36px;
            border-radius: 8px;
            background: rgba(16, 185, 129, 0.15);
            color: #10b981;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .yagna-header h4 {
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--text-main);
        }
        .yagna-target {
            font-size: 0.8rem;
            font-weight: 700;
            color: #10b981;
            margin-bottom: 6px;
        }
        .yagna-desc {
            font-size: 0.86rem;
            color: var(--text-muted);
            line-height: 1.55;
        }

        /* 9 Daily Prayers Interactive Shloka Cards */
        .prayers-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 20px;
            margin: 24px 0;
        }
        .prayer-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }
        .prayer-card:hover {
            border-color: var(--saffron-primary);
            box-shadow: var(--shadow-md);
        }
        .prayer-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }
        .prayer-time-badge {
            background: rgba(245, 158, 11, 0.12);
            color: var(--saffron-primary);
            border: 1px solid rgba(245, 158, 11, 0.3);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 800;
        }
        .btn-copy-shloka {
            background: transparent;
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.76rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            transition: all 0.2s;
        }
        .btn-copy-shloka:hover {
            border-color: var(--saffron-primary);
            color: var(--saffron-primary);
        }
        .prayer-shloka-box {
            background: rgba(0, 0, 0, 0.3);
            border-left: 3px solid var(--saffron-primary);
            padding: 14px 16px;
            border-radius: 0 8px 8px 0;
            font-family: var(--font-heading);
            font-size: 0.96rem;
            line-height: 1.8;
            color: #fef3c7;
            margin-bottom: 12px;
        }
        body.light-theme .prayer-shloka-box {
            background: #fffbeb;
            color: #92400e;
        }
        .prayer-meaning {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.65;
        }
        .prayer-meaning strong {
            color: var(--text-main);
        }

        /* Activity Cards (Full Facilitator Engine) */
        .activity-card-large {
            background: var(--bg-surface);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 36px;
            box-shadow: var(--shadow-md);
            position: relative;
            transition: all 0.25s ease;
        }
        .activity-card-large:hover {
            border-color: var(--saffron-primary);
            box-shadow: var(--shadow-lg);
        }
        .act-header-strip {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 16px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 16px;
        }
        .act-badge-large {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            font-weight: 800;
            padding: 6px 16px;
            border-radius: 999px;
            text-transform: uppercase;
        }
        .act-title-box h3 {
            font-family: var(--font-heading);
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 4px;
        }
        .act-tagline {
            font-size: 0.95rem;
            color: var(--saffron-primary);
            font-weight: 700;
        }

        /* Material List Box */
        .materials-box {
            background: rgba(255, 255, 255, 0.03);
            border: 1px dashed var(--border-color);
            padding: 16px 20px;
            border-radius: var(--radius-md);
            margin: 18px 0 24px 0;
        }
        body.light-theme .materials-box {
            background: #f8fafc;
            border-color: rgba(0, 0, 0, 0.14);
        }
        .materials-title {
            font-size: 0.84rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--saffron-primary);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .materials-items {
            font-size: 0.92rem;
            color: var(--text-main);
            line-height: 1.6;
        }

        /* Steps Container */
        .steps-container {
            margin: 20px 0;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .step-item {
            display: flex;
            gap: 14px;
            align-items: flex-start;
        }
        .step-num {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: rgba(245, 158, 11, 0.15);
            color: var(--saffron-primary);
            border: 1px solid rgba(245, 158, 11, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 0.88rem;
            flex-shrink: 0;
            margin-top: 2px;
        }
        .step-text {
            font-size: 0.95rem;
            line-height: 1.65;
            color: var(--text-muted);
        }
        .step-text strong {
            color: var(--text-main);
        }

        /* Debrief Callout (Aha! Moment) */
        .debrief-box {
            background: rgba(245, 158, 11, 0.08);
            border-left: 4px solid var(--saffron-primary);
            padding: 18px 22px;
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            margin: 20px 0;
        }
        .debrief-title {
            font-size: 0.88rem;
            font-weight: 800;
            color: var(--saffron-primary);
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .debrief-text {
            font-size: 0.94rem;
            font-style: italic;
            color: var(--text-main);
            line-height: 1.7;
        }

        /* Timer Widget */
        .timer-widget {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            padding: 14px 20px;
            border-radius: var(--radius-md);
            margin-top: 22px;
        }
        .timer-display {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--saffron-primary);
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .timer-controls {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .btn-timer {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            font-size: 0.84rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .btn-timer:hover {
            border-color: var(--saffron-primary);
            color: var(--saffron-primary);
        }

        /* Vallalar 44 Sins Filterable Hub */
        .vallalar-filter-bar {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        .btn-v-filter {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-v-filter:hover, .btn-v-filter.active {
            border-color: #ef4444;
            background: rgba(239, 68, 68, 0.15);
            color: #ef4444;
        }
        .vallalar-search-box {
            position: relative;
            margin-bottom: 20px;
        }
        .vallalar-search-input {
            width: 100%;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            padding: 12px 16px 12px 42px;
            border-radius: var(--radius-md);
            color: var(--text-main);
            font-size: 0.95rem;
            outline: none;
            transition: all 0.2s;
        }
        .vallalar-search-input:focus {
            border-color: #ef4444;
            box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2);
        }
        .vallalar-search-icon {
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-dim);
        }

        .vallalar-table-wrap {
            max-height: 480px;
            overflow-y: auto;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            background: var(--bg-surface);
        }
        .vallalar-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
            text-align: left;
        }
        .vallalar-table th {
            background: var(--bg-card);
            padding: 12px 16px;
            font-weight: 800;
            color: var(--text-main);
            border-bottom: 2px solid var(--border-color);
            position: sticky;
            top: 0;
            z-index: 10;
        }
        .vallalar-table td {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            color: var(--text-muted);
            line-height: 1.55;
        }
        .vallalar-table tr:hover td {
            background: rgba(239, 68, 68, 0.04);
            color: var(--text-main);
        }

        /* Sacred Pledge Container */
        .sacred-pledge-card {
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(180, 83, 9, 0.18));
            border: 2px solid #f59e0b;
            border-radius: var(--radius-lg);
            padding: 28px;
            margin: 24px 0;
            box-shadow: 0 8px 30px rgba(245, 158, 11, 0.2);
            position: relative;
        }
        .sacred-pledge-card::before {
            content: '🙏 அறம் காக்கும் ஷட் கர்ம சங்கல்பம் (Sacred Pledge)';
            position: absolute;
            top: -14px;
            left: 24px;
            background: #d97706;
            color: #ffffff;
            padding: 2px 16px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 800;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
        .pledge-text {
            font-size: 1.05rem;
            line-height: 1.9;
            color: #fffbeb;
            font-weight: 600;
            background: rgba(0, 0, 0, 0.3);
            padding: 20px 24px;
            border-radius: var(--radius-md);
            border-left: 4px solid #f59e0b;
            margin-bottom: 16px;
        }
        body.light-theme .pledge-text {
            background: rgba(245, 158, 11, 0.1);
            color: #78350f;
        }

        /* Checklists */
        .checklist-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin: 24px 0;
        }
        .checklist-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 22px;
        }
        .checklist-card h4 {
            font-size: 1.05rem;
            font-weight: 800;
            margin-bottom: 14px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .check-item {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin-bottom: 12px;
            cursor: pointer;
            font-size: 0.9rem;
            color: var(--text-muted);
            line-height: 1.5;
        }
        .check-item input[type="checkbox"] {
            margin-top: 3px;
            width: 17px;
            height: 17px;
            accent-color: var(--saffron-primary);
            cursor: pointer;
            flex-shrink: 0;
        }
        .check-item:hover {
            color: var(--text-main);
        }

        /* Self-Audit Quiz Container */
        .quiz-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 28px;
            margin: 24px 0;
        }
        .quiz-q-block {
            margin-bottom: 24px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 20px;
        }
        .quiz-q-title {
            font-size: 1rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .quiz-opt-label {
            display: flex;
            align-items: center;
            gap: 10px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            padding: 10px 16px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            font-size: 0.9rem;
            color: var(--text-muted);
            transition: all 0.2s;
        }
        .quiz-opt-label:hover {
            border-color: var(--saffron-primary);
            color: var(--text-main);
        }
        .quiz-opt-label input[type="radio"] {
            accent-color: var(--saffron-primary);
        }
        .quiz-result-box {
            display: none;
            background: rgba(245, 158, 11, 0.12);
            border: 2px solid var(--saffron-primary);
            border-radius: var(--radius-md);
            padding: 22px;
            margin-top: 20px;
            text-align: center;
        }

        /* Footer */
        .footer {
            border-top: 1px solid var(--border-color);
            padding: 40px 0;
            background: var(--bg-surface);
            text-align: center;
            color: var(--text-dim);
            font-size: 0.88rem;
        }

        /* Print styles */
        @media print {
            .navbar, .section-anchor-bar, .timer-widget, .nav-actions, .btn-v-filter, .vallalar-search-box {
                display: none !important;
            }
            body {
                background: #ffffff !important;
                color: #000000 !important;
            }
            .activity-card-large, .tie-card, .karma-card, .prayer-card {
                border: 1px solid #999 !important;
                box-shadow: none !important;
                page-break-inside: avoid;
            }
        }

        @media (max-width: 768px) {
            .navbar-inner {
                flex-direction: column;
                align-items: flex-start;
            }
            .nav-actions {
                width: 100%;
                justify-content: flex-end;
            }
            .activity-card-large {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
"""

print("Writing Part 1...")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(head_and_css)

print("Part 1 written successfully.")
