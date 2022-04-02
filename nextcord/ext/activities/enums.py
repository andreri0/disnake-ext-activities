from enum import Enum


class ActivityBase(Enum):
    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.value or 0


class Activity(ActivityBase):
    """These are activities can be playable."""

    # you can insert activity_id parameter while setting this as activities,
    # honestly very useless since nextcord already have target_application_id, but heck yeah

    custom = None
    """Represent an custom activity."""

    betrayal = 773336526917861400
    """Represent the betrayal.io game."""

    fishington = 814288819477020702
    """Represent the fishington game."""

    youtube = 880218394199220334
    """Represent the Watch Together activity.
        .. note::
            This has an alias for legacy compability (:attr:`enums.Activity.watch_together`)."""

    doodle = 878067389634314250
    """Represent the Doodle Crew activity.
        .. warning::
            This activity is deprecated and you should use :attr:`enums.Activity.sketch` instead."""

    sketch = 902271654783242291
    """Represent the Sketch Heads activity."""

    word_snacks = 879863976006127627
    """Represent the word snacks activity."""

    blazing = 832025144389533716
    """Represent the Blazing 8s activity.
        .. note::
            This has an alias for legacy compability (:attr:`enums.Activity.ocho`)."""

    putt_party = 945737671223947305
    """Represent the Putt Party activity."""

    land_io = 903769130790969345
    """Represent the Land.io activity."""

    # Potential boost locked

    poker = 755827207812677713  # boost-locked
    """Represent the Poker Night activity.
        .. note::
            This is boost-locked. To start this activity, you need to have tier 1 boosting or have the `HAD_EARLY_ACTIVITY_ACCESS` feature."""

    chess = 832012774040141894
    """Represent the Chess In The Park activity.
        .. note::
            This is boost-locked. To start this activity, you need to have tier 1 boosting or have the `HAD_EARLY_ACTIVITY_ACCESS` feature."""  # boost-locked

    checker = 832013003968348200  # boost-locked
    """Represent the Checkers in the park activity.
        .. note::
            This is boost-locked. To start this activity, you need to have tier 1 boosting or have the `HAD_EARLY_ACTIVITY_ACCESS` feature."""

    spellcast = 852509694341283871  # boost-locked
    """Represent the Spellcase activity.
        .. note::
            1. This is boost-locked. To start this activity, you need to have tier 1 boosting or have the `HAD_EARLY_ACTIVITY_ACCESS` feature.
            2. This has an alias (:attr:`enums.Activity.checkers`) for spelling stuff."""

    letter_league = 879863686565621790  # boost-locked
    """Represent the Letter League activity.
        .. note::
            1. This is boost-locked. To start this activity, you need to have tier 1 boosting or have the `HAD_EARLY_ACTIVITY_ACCESS` feature.
            2. This has an alias (:attr:`enums.Activity.letter_tile`) for legacy compability."""

    awkword = 879863881349087252  # boost-locked
    """Represent the Awkword activity.
        .. note::
            This is boost-locked. To start this activity, you need to have tier 1 boosting or have the `HAD_EARLY_ACTIVITY_ACCESS` feature."""

    # aliases for legacy reasons
    letter_tile = letter_league  # boost-locked, now named letter_league
    ocho = blazing  # boost-locked
    watch_together = youtube
    checkers = checker


# https://gist.github.com/GeneralSadaf/42d91a2b6a93a7db7a39208f2d8b53ad#development-versions
class ActivityDevelopment(ActivityBase):
    """These are development versions of the activities. May not be playable."""

    putt_party = 910224161476083792
    """Represent the Putt Party Development activity.
        .. note::
            This is an development version and may be unplayable."""
    sketch = 879864104980979792
    """Represent the Sketch Heads Development activity.
        .. note::
            This is an development version and may be unplayable."""
    doodle = 878067427668275241
    """Represent the Doodle Crew Development activity.
        .. note::   
            This is an development version and may be unplayable."""
    youtube = 880218832743055411
    """Represent the Watch Together Development activity.
    .. note::   
        This is an development version and may be unplayable."""

    PN = 763133495793942528
    """Represent the Poker Night Development activity.
        .. note::   
            This is an development version and may be unplayable."""
    word_snacks = 879864010126786570
    """Represent the Word Snacks Development activity.
        .. note::
            This is an development version and may be unplayable."""
    decoder = 891001866073296967
    """Represent the Decoder Development activity.
        .. note::
            This is an development version and may be unplayable."""
