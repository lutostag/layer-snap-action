from charms.reactive import when, when_not, set_state


@when_not('layer-snap-action.installed')
def install_layer_snap_action():
    set_state('layer-snap-action.installed')
