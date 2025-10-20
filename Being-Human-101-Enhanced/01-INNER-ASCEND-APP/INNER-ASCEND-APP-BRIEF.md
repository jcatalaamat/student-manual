# INNER ASCEND: App Brief
## Quick Handoff Document for New Sessions

---

## WHAT IS IT? (One sentence)

**Inner Ascend is a daily spiritual practice app that combines Co-Star's cosmic guidance with a structured 90-day shadow work curriculum (Being Human 101), guided meditations, journaling, and progress tracking—all in a dark, immersive, Pinterest-worthy mobile experience.**

---

## THE NICHE POSITION

**"Co-Star meets Insight Timer meets Mindvalley—but make it Shadow Work"**

| Feature | Co-Star | Insight Timer | Mindvalley | **INNER ASCEND** |
|---------|---------|---------------|------------|------------------|
| Daily cosmic guidance | ✅ | ❌ | ❌ | ✅ |
| Structured curriculum | ❌ | ❌ | ✅ | ✅ |
| Guided meditations | ❌ | ✅ | ✅ | ✅ |
| Shadow work focus | ❌ | ❌ | ❌ | ✅ |
| Journaling + tracking | ❌ | Basic | ❌ | ✅ |
| Price | $15/mo | $60/yr | $499/yr | **$17/mo** |

**You are the ONLY app combining daily cosmic context + structured shadow work journey + guided practices + journaling in one cohesive system.**

---

## THE MVP: 6 CORE SCREENS

### 1. **TODAY (Home)**
- Daily cosmic weather (moon phase, planetary transits)
- Today's shadow work focus (from Being Human 101 curriculum)
- Guided practice button (meditation or exercise)
- Emotional check-in (4 states: struggling, processing, clear, integrated)
- Streak counter (gamification)

### 2. **JOURNEY (Curriculum)**
- Being Human 101: 16 modules displayed as cards
- Each module shows: Title, signature image, progress %, days completed
- Completed modules glow green, active glows purple, locked are dimmed
- Tap module to enter deep dive

### 3. **MODULE VIEW**
- Today's teaching (text from Being Human 101)
- Today's practices (meditation, exercises, journaling)
- Mark day complete button
- Progress bar showing module completion

### 4. **PRACTICES LIBRARY**
- All 7 guided meditations (audio player with waveform)
- All journaling prompts (organized by theme)
- All exercises (projection tracker, parts dialogue, etc.)
- Can access standalone or within module flow

### 5. **PROGRESS**
- Current streak + longest streak
- Circular progress ring showing days practiced
- Modules completed (visual timeline with dots)
- Practice breakdown (meditations, journaling, exercises count)
- Achievement badges (milestone unlocks)

### 6. **JOURNALING**
- Daily prompt from current module
- Minimal distraction text editor
- Word count + timer (live)
- Auto-save
- Access to previous entries

---

## VISUAL AESTHETIC: "COSMIC DEPTH"

**NOT:** White backgrounds, pastel colors, stock photos of people meditating

**YES:**
- **Dark palette:** Deep space blacks (#0A0A0F), cosmic violet (#8B7BF7), silver moon text (#E8E6F0)
- **Full-screen immersive imagery:** Space photography, natural textures, abstract metaphors
- **Glassmorphism:** Apple-style blurred glass cards with depth
- **Glow effects:** Subtle purple glows on active states, progress, completions
- **Custom illustrations:** Emotion icons, achievement badges, meditation symbols
- **Layered composition:** Background image → gradient overlay → glass cards → content → floating particles
- **Smooth animations:** Parallax scrolling, slow zoom on images, live audio waveforms, particle systems

**Three visual themes rotating:**
1. **Cosmic/Celestial** (space, nebulas, moon phases) - for astrology
2. **Natural Textures** (obsidian, water, fabric, plants) - for grounding/modules
3. **Abstract/Metaphorical** (ink in water, shadows, reflections) - for emotions/practices

**Pinterest-worthy on every screen.**

---

## CONTENT (Already Written)

✅ **Being Human 101:** 16 modules, 12,558 lines of content (already complete)
✅ **Meditation scripts:** 7 guided practices (already written)
✅ **Journaling prompts:** 100+ prompts across all modules (already written)
✅ **Exercises:** Shadow work tools, projection tracker, parts dialogue (already written)

**No content creation needed—just implementation.**

---

## TECH STACK

- **Frontend:** React Native + Expo + Tamagui (performance + beautiful UI)
- **Backend:** Supabase (database, auth, storage)
- **Astrology:** AstroAPI or Astrology.js library
- **Audio:** Expo AV (meditation player)
- **Payments:** RevenueCat (subscriptions)
- **Animations:** Reanimated 2, React Native Skia (particles, gradients)
- **Visuals:** React Native Blur, Expo Linear Gradient, Lottie

**Build time:** 12 weeks (3 months) solo with Claude Code

---

## PRICING MODEL

**Freemium:**
- **FREE:** Module 1 (Awakening), daily cosmic weather, 2 meditations, basic progress tracking
- **PREMIUM ($17/mo or $147/yr):** All 16 modules, all 7 meditations, all prompts, full tracking, personalized guidance

**Why this works:**
- Cheaper than Co-Star ($15/mo) + therapy
- Cheaper than Mindvalley ($499/yr)
- Free tier lets users taste the teaching before committing

---

## REVENUE PROJECTIONS

**Conservative (10% free → paid conversion):**

| Timeline | Total Users | Premium Users | Monthly Revenue | Annual Revenue |
|----------|-------------|---------------|-----------------|----------------|
| Month 3 | 500 | 50 | $850 | - |
| Month 6 | 1,500 | 150 | $2,550 | - |
| Month 12 | 5,000 | 500 | $8,500 | **$51,000** |
| Year 2 | 15,000 | 1,500 | $25,500 | **$204,000** |

**If you scale to Insight Timer levels (even 0.5% of their 20M users paying):**
- 100,000 premium × $17/mo = **$1.7M/month** = **$20.4M/year**

---

## KEY DIFFERENTIATORS

1. **Only app combining cosmic context + shadow work curriculum**
2. **Structured 90-day journey (not overwhelming library)**
3. **Dark, immersive, mystical aesthetic (not clinical/sterile)**
4. **One cohesive teaching (not 50 different teachers)**
5. **Affordable ($17/mo vs $499/yr for Mindvalley)**
6. **Built for transformation, not consumption**

---

## WHAT'S ALREADY DOCUMENTED

1. **INNER-ASCEND-NICHE-MVP.md** - Full MVP spec, market gap, features, revenue
2. **INNER-ASCEND-VISUAL-DESIGN-SYSTEM.md** - Color palette, typography, spacing, shadows, icons, micro-interactions
3. **INNER-ASCEND-VISUAL-IMAGERY-LAYOUT.md** - Full imagery strategy, screen layouts with images, sourcing, animation

All in: `/Users/astralamat/Downloads/Student Manual/Being-Human-101-Enhanced/`

---

## NEXT STEPS (If Building)

**Phase 1: Design (Weeks 1-2)**
- [ ] Create Pinterest mood board (50-100 pins)
- [ ] Source all module signature images (16 images)
- [ ] Commission custom illustrations (emotion icons, badges)
- [ ] Design 6 screens in Figma (with design system applied)

**Phase 2: Build Core (Weeks 3-8)**
- [ ] Set up React Native + Expo + Tamagui + Supabase
- [ ] Build 6 core screens (static first)
- [ ] Import Being Human 101 content into database
- [ ] Implement astrology API integration
- [ ] Build module progression logic
- [ ] Add audio player for meditations
- [ ] Build journaling system

**Phase 3: Polish + Launch (Weeks 9-12)**
- [ ] Implement animations (particles, parallax, glow effects)
- [ ] Add push notifications (daily reminders)
- [ ] Set up RevenueCat (subscription paywall)
- [ ] Beta test with 20-50 users
- [ ] Record meditation audio (or use TTS)
- [ ] Submit to App Store + Google Play

**Timeline:** 12 weeks total

---

## MARKETING POSITIONING

**Tagline:**
> "Daily spiritual practice meets deep shadow work—guided by astrology, rooted in transformation."

**Elevator Pitch:**
> "Co-Star tells you what the stars are doing. Insight Timer gives you 100,000 meditations. Mindvalley sells you 50 courses. Inner Ascend gives you ONE structured 90-day journey through shadow work, inner child healing, and embodiment—personalized to your cosmic weather, with daily practices that actually integrate."

**Who it's for:**
- People who love Co-Star but want MORE than daily astrology
- People overwhelmed by Insight Timer's massive library
- People who can't afford Mindvalley ($499/year)
- Shadow work seekers who want structure + accountability + cosmic context

**App Store keywords:**
Shadow work, astrology app, daily spiritual practice, inner child healing, meditation app, mindfulness, personal growth, self-discovery, cosmic guidance, transformation journey

---

## QUESTIONS TO ASK NEW CLAUDE

**If continuing design:**
- "Help me create a Figma design system based on INNER-ASCEND-VISUAL-DESIGN-SYSTEM.md"
- "Help me source the 16 module signature images from Unsplash based on the visual themes"
- "Help me write prompts for commissioning custom illustrations on Fiverr"

**If starting to build:**
- "Help me set up React Native + Expo + Tamagui + Supabase for Inner Ascend"
- "Help me build the Today screen based on the design specs"
- "Help me structure the Supabase database for Being Human 101 modules"

**If refining strategy:**
- "Help me create a content calendar for organic Instagram marketing"
- "Help me plan beta testing strategy for Inner Ascend"
- "Help me create onboarding flow for new users"

---

## TL;DR FOR NEW CLAUDE

**Inner Ascend = Co-Star + Insight Timer + Mindvalley for shadow work.**

Daily cosmic guidance + 90-day Being Human 101 curriculum + guided meditations + journaling + progress tracking.

Dark, immersive, Pinterest-worthy design. $17/mo. Content already written. 3-month solo build with Claude Code.

**The only app doing this.** Blue ocean opportunity.

All docs in `/Users/astralamat/Downloads/Student Manual/Being-Human-101-Enhanced/`

🚀
