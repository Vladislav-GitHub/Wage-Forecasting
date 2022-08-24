document.addEventListener('DOMContentLoaded', () => {

    const followCursor = () => { // declare function followCursor
      const el = document.querySelector('.follow-cursor') // search element

      window.addEventListener('mousemove', e => { // when we move the cursor
        const target = e.target // locate where is the cursor
        if (!target) return

        if (target.closest('a')) { // if cursor close to link
          el.classList.add('follow-cursor_active') // add active class to element
        } else {
          el.classList.remove('follow-cursor_active') // delete active class
        }

        el.style.left = e.pageX + 'px' // determine positioning from left
        el.style.top = e.pageY + 'px' // determine positioning from up
      })
    }

    followCursor() // call function followCursor

  })