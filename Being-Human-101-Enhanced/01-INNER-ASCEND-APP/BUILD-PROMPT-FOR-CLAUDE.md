# INITIAL BUILD PROMPT FOR CLAUDE CODE
## Copy/paste this to start building the Inner Ascend app

---

## THE PROMPT

```
I need you to build the skeleton structure for Inner Ascend - a React Native mobile app.

CONTEXT:
Inner Ascend is a daily spiritual practice app combining Co-Star-style cosmic guidance
with a structured 90-day shadow work curriculum (Being Human 101). Think: Co-Star +
Insight Timer + Mindvalley, but for shadow work.

Full specs are in:
- /Users/astralamat/Downloads/Student Manual/Being-Human-101-Enhanced/01-INNER-ASCEND-APP/INNER-ASCEND-APP-BRIEF.md
- /Users/astralamat/Downloads/Student Manual/Being-Human-101-Enhanced/01-INNER-ASCEND-APP/INNER-ASCEND-NICHE-MVP.md
- /Users/astralamat/Downloads/Student Manual/Being-Human-101-Enhanced/01-INNER-ASCEND-APP/INNER-ASCEND-VISUAL-DESIGN-SYSTEM.md

PLEASE:
1. Read those 3 files to understand the app concept and design system
2. Set up a new React Native project with Expo + Tamagui
3. Create the complete folder structure and navigation skeleton
4. Build empty component files for all 6 core screens with placeholder content
5. Set up the design system (colors, typography, spacing from VISUAL-DESIGN-SYSTEM.md)
6. Configure the tab navigation structure
7. DO NOT implement full features yet - just skeleton/structure

TECH STACK:
- React Native + Expo (latest)
- Tamagui (UI library)
- React Navigation (tab + stack navigation)
- TypeScript

APP STRUCTURE (6 core screens):

1. TODAY (Home) - Tab 1
   - Daily cosmic weather display
   - Today's shadow work focus
   - Practice button
   - Emotional check-in (4 states)
   - Streak counter

2. JOURNEY (Curriculum) - Tab 2
   - List of 16 modules as cards
   - Each module shows: title, image placeholder, progress, status (completed/active/locked)

3. MODULE VIEW (Stack screen - accessed from Journey)
   - Module title + progress
   - Today's teaching section
   - Practices list
   - Journaling section
   - Mark complete button

4. PRACTICES LIBRARY - Tab 3
   - Tabs: Meditations / Journaling / Exercises
   - List of practices
   - Audio player placeholder for meditations

5. PROGRESS - Tab 4
   - Circular progress ring (placeholder)
   - Streak counter
   - Module completion dots
   - Practice breakdown stats
   - Achievement badges section

6. JOURNALING (Stack screen - accessed from Module View or Practices)
   - Prompt display
   - Text input area
   - Word count + timer
   - Save button

NAVIGATION STRUCTURE:
- Bottom tab navigation (4 tabs: Today, Journey, Practices, Progress)
- Stack navigation for: Module View, Journaling, Meditation Player
- Tab icons: Use simple placeholders for now

DESIGN SYSTEM TO IMPLEMENT:
Colors (from VISUAL-DESIGN-SYSTEM.md):
- Background: #0A0A0F (deep space black)
- Card background: #121218
- Elevated surfaces: #1A1A24
- Primary accent: #8B7BF7 (cosmic violet)
- Text primary: #E8E6F0 (silver moon)
- Text secondary: #B8B5C8
- Success green: #4ECDC4

Typography:
- Headings: Libre Baskerville (you can use system serif as placeholder)
- Body: Inter (or system sans-serif as placeholder)
- Numbers/stats: Monospace

Spacing system (8px base):
- xs: 8px
- sm: 16px
- md: 24px
- lg: 32px
- xl: 48px

FOLDER STRUCTURE TO CREATE:
```
inner-ascend/
├── app/                          # Expo Router app directory
│   ├── (tabs)/                   # Tab navigation group
│   │   ├── index.tsx             # Today screen (tab 1)
│   │   ├── journey.tsx           # Journey screen (tab 2)
│   │   ├── practices.tsx         # Practices screen (tab 3)
│   │   └── progress.tsx          # Progress screen (tab 4)
│   ├── module/[id].tsx           # Module detail screen (stack)
│   ├── journaling.tsx            # Journaling screen (stack)
│   └── _layout.tsx               # Root layout with tabs
├── components/                   # Reusable components
│   ├── cards/
│   │   ├── ModuleCard.tsx        # Module cards for Journey screen
│   │   ├── PracticeCard.tsx      # Practice cards
│   │   └── StatsCard.tsx         # Stats display cards
│   ├── ui/
│   │   ├── Button.tsx            # Custom button component
│   │   ├── ProgressRing.tsx      # Circular progress component
│   │   ├── StreakCounter.tsx     # Streak display
│   │   └── EmotionalCheckIn.tsx  # 4-state emotion selector
│   └── layouts/
│       ├── Screen.tsx            # Base screen wrapper
│       └── Card.tsx              # Glass card wrapper
├── constants/
│   ├── Colors.ts                 # Color palette
│   ├── Typography.ts             # Font styles
│   └── Spacing.ts                # Spacing system
├── types/
│   ├── Module.ts                 # Module type definitions
│   ├── Practice.ts               # Practice type definitions
│   └── Progress.ts               # Progress tracking types
└── data/
    └── modules.ts                # Mock module data (16 modules)
```

WHAT TO BUILD NOW:
1. Initialize Expo project with TypeScript
2. Install dependencies: Expo, Tamagui, React Navigation
3. Create all folders and empty component files
4. Set up design system constants (colors, typography, spacing)
5. Implement basic tab navigation with placeholder screens
6. Create base components (Button, Card, Screen wrapper)
7. Add mock data for 16 modules (just title, id, duration, status)
8. Make each screen render with:
   - Screen title
   - Placeholder text describing what will go here
   - Basic layout structure (no real functionality)

EXAMPLE OF WHAT A SKELETON SCREEN SHOULD LOOK LIKE:

```tsx
// app/(tabs)/index.tsx - Today Screen
import { View, Text } from 'tamagui'
import { Screen } from '@/components/layouts/Screen'

export default function TodayScreen() {
  return (
    <Screen>
      <Text fontSize="$8" fontWeight="bold" color="$textPrimary">
        TODAY
      </Text>

      {/* Cosmic Weather Section - Placeholder */}
      <View marginTop="$4" padding="$4" backgroundColor="$cardBg">
        <Text color="$textSecondary">
          [Cosmic Weather Display - To be implemented]
        </Text>
      </View>

      {/* Shadow Work Focus - Placeholder */}
      <View marginTop="$4" padding="$4" backgroundColor="$cardBg">
        <Text color="$textSecondary">
          [Today's Shadow Work Focus - To be implemented]
        </Text>
      </View>

      {/* Emotional Check-In - Placeholder */}
      <View marginTop="$4" padding="$4" backgroundColor="$cardBg">
        <Text color="$textSecondary">
          [Emotional Check-In (4 states) - To be implemented]
        </Text>
      </View>

      {/* Streak Counter - Placeholder */}
      <View marginTop="$4" padding="$4" backgroundColor="$cardBg">
        <Text color="$textSecondary">
          [Streak Counter: 🔥 23 days - To be implemented]
        </Text>
      </View>
    </Screen>
  )
}
```

AFTER YOU'VE BUILT THE SKELETON:
1. Show me the complete folder structure you created
2. Show me one example screen file to confirm the structure is correct
3. Confirm the app runs with `npx expo start`
4. Ask me which screen/feature I want you to implement first

DO NOT:
- Implement full features yet (no API calls, no real data, no complex logic)
- Add images or assets (use placeholders)
- Set up Supabase or any backend (that's later)
- Implement authentication (that's later)
- Build the audio player (that's later)
- Create custom fonts setup (system fonts for now)

JUST BUILD THE SKELETON so we have a solid foundation to build on.

Ready to start?
```

---

## FOLLOW-UP PROMPTS (After skeleton is built)

### AFTER SKELETON IS COMPLETE:

```
Great! The skeleton looks good. Now let's implement the Today screen fully.

Please:
1. Read the Being Human 101 content structure from:
   /Users/astralamat/Downloads/Student Manual/Being-Human-101-Enhanced/Part-1-Foundations/

2. Implement the Today screen with:
   - Mock cosmic weather data (just hardcoded for now)
   - Display today's module + day number
   - Functional emotional check-in (4 buttons, save state)
   - Functional streak counter (mock data, just display)
   - Glass card styling from VISUAL-DESIGN-SYSTEM.md

3. Add proper styling with:
   - Glassmorphism effect on cards
   - Glow effects on interactive elements
   - Proper spacing from design system
   - Dark cosmic background

Show me the implementation when done.
```

### AFTER TODAY SCREEN:

```
Excellent. Now let's build the Journey screen.

Please:
1. Create ModuleCard component with:
   - Module title
   - Progress bar (0-100%)
   - Status indicator (completed ✅ / active 🔥 / locked 🔒)
   - Tap to navigate to Module View
   - Different visual states for completed/active/locked

2. Display all 16 modules from Being Human 101:
   - Module 1: Awakening (7 days)
   - Module 2: Core Wounds (7 days)
   - Module 3: Shadow Work (14 days)
   - Module 4: Inner Child Healing (14 days)
   - [etc. - get titles from Part-1-Foundations, Part-2-Deep-Work, Part-3-Mastery-Integration folders]

3. Implement navigation to Module View screen when card is tapped

4. Style according to design system (glass cards, glow effects for active module)

Show me the implementation.
```

### CLEANING UP OLD FILES:

```
Now that we have the skeleton built and you've referenced all the design docs,
please clean up:

1. Move these reference docs to an ARCHIVE folder:
   - INNER-ASCEND-LANDING-PAGE-REDESIGN.md (not needed for app build)
   - INNER-ASCEND-VISUAL-IMAGERY-LAYOUT.md (reference complete)

2. Keep these files accessible (we'll need them):
   - INNER-ASCEND-APP-BRIEF.md (quick reference)
   - INNER-ASCEND-NICHE-MVP.md (feature specs)
   - INNER-ASCEND-VISUAL-DESIGN-SYSTEM.md (ongoing reference)

3. Create a new BUILD-LOG.md to track what's been implemented and what's next

4. Delete any duplicate or outdated files from previous explorations
```

---

## TIPS FOR WORKING WITH CLAUDE CODE

### When starting each session:

```
I'm building Inner Ascend app. Current status in:
/path/to/inner-ascend/BUILD-LOG.md

Last session we implemented: [X]
Today I want to implement: [Y]

Please read BUILD-LOG.md and continue from there.
```

### When you want to see progress:

```
Can you:
1. Run the app (`npx expo start`)
2. Take a screenshot or describe what's currently visible
3. Show me the current folder structure
4. Update BUILD-LOG.md with what we've completed today
```

### When you want to implement a new feature:

```
Let's implement [FEATURE NAME].

Reference:
- Design specs: INNER-ASCEND-VISUAL-DESIGN-SYSTEM.md (section X)
- Content: Being-Human-101-Enhanced/[relevant folder]

Build it step by step:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Show me each step before moving to the next.
```

---

## BUILD PRIORITY ORDER (Recommended)

After skeleton is complete, build in this order:

1. **Today Screen** (core experience, shows immediate value)
2. **Journey Screen** (shows full curriculum, navigation to modules)
3. **Module View Screen** (delivers the content)
4. **Progress Screen** (gamification, retention)
5. **Practices Library** (standalone practice access)
6. **Journaling Screen** (integration tool)
7. **Polish & Animations** (glassmorphism, glow effects, particles)
8. **Backend Integration** (Supabase, auth, data persistence)
9. **Audio Player** (meditation playback)
10. **Astrology Integration** (cosmic weather API)

---

## FOLDER CLEANUP AFTER INITIAL BUILD

Once Claude has built the skeleton and referenced the design docs, have it create:

```
inner-ascend/
├── app/                    # Your built app
├── docs/                   # Keep these
│   ├── INNER-ASCEND-APP-BRIEF.md
│   ├── INNER-ASCEND-NICHE-MVP.md
│   └── INNER-ASCEND-VISUAL-DESIGN-SYSTEM.md
├── docs/archive/           # Move here after referenced
│   ├── INNER-ASCEND-LANDING-PAGE-REDESIGN.md
│   ├── INNER-ASCEND-ONE-PAGE-WEB.md
│   └── INNER-ASCEND-VISUAL-IMAGERY-LAYOUT.md
└── BUILD-LOG.md            # Track progress here
```

---

## FINAL NOTES

**This prompt will:**
✅ Get Claude to read your complete specs
✅ Set up the entire project structure
✅ Create all navigation and screen files
✅ Implement the design system
✅ Give you a running skeleton app
✅ Prepare for feature-by-feature implementation

**After skeleton is done:**
✅ You'll have a working app (just with placeholders)
✅ All 6 screens accessible via navigation
✅ Design system colors/typography applied
✅ Ready to implement features one by one

**Time estimate:**
- Skeleton setup: 30-60 minutes
- Each screen implementation: 1-3 hours
- Total MVP: 12-20 hours of Claude Code sessions

Start with the main prompt above and go! 🚀
